# -*- coding: utf-8 -*-
from django.db import models


class SoftwareInstalledManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except SoftwareInstalled.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except SoftwareInstalled.DoesNotExist:
            return None
        return instance


class SoftwareInstalled(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.CharField(
        default='',
        max_length=128)
    description = models.TextField(
        default='',
        null=True,
        blank=True)

    objects = SoftwareInstalledManager()

    class Meta:
        db_table = 'hpc_software_installed'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class SoftwareVersion(models.Model):
    id = models.AutoField(
        primary_key=True)
    version = models.CharField(
        default='',
        max_length=128)
    software = models.ForeignKey(
        SoftwareInstalled,
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'hpc_software_version'
        ordering = ['id', ]

    def __str__(self):
        return self.version


class SoftwareRequestedManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except SoftwareRequested.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except SoftwareRequested.DoesNotExist:
            return None
        return instance


class SoftwareRequested(models.Model):
    id = models.AutoField(
        primary_key=True)
    software = models.CharField(
        default='',
        max_length=128)
    website = models.URLField()
    version = models.CharField(
        default='',
        max_length=128,
        null=True,
        blank=True)
    type = models.CharField(
        default='',
        max_length=128)
    installation_guide = models.URLField()
    motivation = models.TextField()
    account = models.CharField(
        max_length=100)
    requested = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True)

    objects = SoftwareRequestedManager()

    class Meta:
        db_table = 'hpc_software_requested'
        ordering = ['id', ]

    def __str__(self):
        return self.software
