# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils import translation
import uuid
import os

___DOCUMENT_FOLDER_PATH___ = 'application/home/document'


class DocumentManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except Document.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except Document.DoesNotExist:
            return None
        return instance


class Document(models.Model):
    def ___IMAGE_UPLOAD_TO___(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(___DOCUMENT_FOLDER_PATH___, filename)

    id = models.AutoField(
        primary_key=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    title_en = models.CharField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    title_es = models.CharField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    content_en = models.TextField(
        default='',
        null=True,
        blank=True,
    )
    content_es = models.TextField(
        default='',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=___IMAGE_UPLOAD_TO___,
    )

    objects = DocumentManager()

    class Meta:
        db_table = 'application___home___document'
        ordering = ['id', ]

    def __str__(self):
        if translation.get_language() == 'en':
            return '%(title)s' % {'title': self.title_en, }
        elif translation.get_language() == 'es':
            return '%(title)s' % {'title': self.title_es, }
        else:
            return '%(id)s' % {'id': self.id, }

    def ___string___content___(self):
        if translation.get_language() == 'en':
            return '%(content)s' % {'content': self.content_en, }
        elif translation.get_language() == 'es':
            return '%(content)s' % {'content': self.content_es, }
        else:
            return '%(content)s' % {'content': '', }

    def ___string___file_path___(self):
        return os.path.join(settings.MEDIA_ROOT, ___DOCUMENT_FOLDER_PATH___, self.image.url)
