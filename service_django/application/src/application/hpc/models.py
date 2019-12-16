# -*- coding: utf-8 -*-
from django.db import models


class Module(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.CharField(
        default='',
        max_length=128)
    description = models.TextField(
        default='',
        null=True,
        blank=True)

    class Meta:
        db_table = 'hpc_module'
        ordering = ['name', ]


class Version(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.CharField(
        default='',
        max_length=128)
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hpc_module_version'
        ordering = ['id', ]
