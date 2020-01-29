# -*- coding: utf-8 -*-
from django.db import models


class Node(models.Model):
    id = models.AutoField(
        primary_key=True,
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
    name = models.CharField(
        default='',
        max_length=100,
    )
    usr = models.FloatField(
        max_length=100
    )
    nice = models.FloatField(
        max_length=100
    )
    sys = models.FloatField(
        max_length=100
    )
    iowait = models.FloatField(
        max_length=100
    )
    irq = models.FloatField(
        max_length=100
    )
    soft = models.FloatField(
        max_length=100
    )
    steal = models.FloatField(
        max_length=100
    )
    guest = models.FloatField(
        max_length=100
    )
    gnice = models.FloatField(
        max_length=100
    )
    idle = models.FloatField(
        max_length=100
    )

    # objects = NodesManager()

    class Meta:
        db_table = 'application___statistic___node'
        ordering = ['id', ]

    def __str__(self):
        return self.name
