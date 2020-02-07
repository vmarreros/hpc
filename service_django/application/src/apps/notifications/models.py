from django.db import models
from django.db.models import query
from django.utils import timezone

from src.apps.security.models import LDAPUser, LDAPUserImported


class AlertManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except Alert.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except Alert.DoesNotExist:
            return None
        return instance

    def unread(self):
        """Return only unread items in the current queryset"""
        return self.filter(unread=True)

    def read(self):
        """Return only read items in the current queryset"""
        return self.filter(unread=False)

    def mark_all_as_read(self, ldap_user=None, ldap_imported_user=None):
        """Mark as read any unread messages in the current queryset.
        Optionally, filter these by recipient first.
        """
        qset = self.unread()

        if ldap_user:
            qset = qset.filter(ldap_user=ldap_user)

        if ldap_imported_user:
            qset = qset.filter(ldap_imported_user=ldap_imported_user)

        return qset.update(unread=False)

    def mark_all_as_unread(self, ldap_user=None, ldap_imported_user=None):
        """Mark as unread any read messages in the current queryset.
        Optionally, filter these by recipient first.
        """
        qset = self.read()

        if ldap_user:
            qset = qset.filter(ldap_user=ldap_user)

        if ldap_imported_user:
            qset = qset.filter(ldap_imported_user=ldap_imported_user)

        return qset.update(unread=True)

    def get_alerts_by_user(self, request):
        instances = self.filter(to_ldap_user__in=[request.security_user])
        return instances

    def get_alerts_unread_by_user(self, request):
        instances = self.filter(to_ldap_user__in=[request.security_user]).filter(unread=True)
        return instances


class Alert(models.Model):
    LEVELS = (
        ('success', 'success'),
        ('info', 'info'),
        ('warning', 'warning'),
        ('error', 'error'))
    level = models.CharField(
        choices=LEVELS,
        default='info',
        max_length=20)
    from_user = models.ForeignKey(
        LDAPUser,
        related_name="from_user",
        on_delete=models.CASCADE)
    to_ldap_user = models.ManyToManyField(
        LDAPUser,
        blank=True)
    to_ldap_imported_user = models.ManyToManyField(
        LDAPUserImported,
        blank=True)
    subject = models.CharField(
        max_length=255)
    message = models.TextField()
    unread = models.BooleanField(
        default=True,
        blank=False,
        db_index=True)
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        db_index=True)
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True)

    objects = AlertManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.subject

    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_
        return timesince_(self.created, now)

    def mark_as_read(self):
        if self.unread:
            self.unread = False
            self.save()

    def mark_as_unread(self):
        if not self.unread:
            self.unread = True
            self.save()
