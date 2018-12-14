# -*- coding: utf-8 -*-
from . import models
from celery import shared_task
import random


@shared_task()
def statistic_generator():
    names_node = ["nodo-dev01", "nodo-dev02", "nodo-dev03", "nodo-dev04", "nodo-dev05", "nodo-dev06"]
    for name in names_node:
        statistics_node = models.Node.objects.filter(name=name)
        if statistics_node.count() >= 13:
            node = statistics_node.first()
            node.delete()
    for name in names_node:
        models.Node(
            name=name,
            usr=random.randrange(100),
            nice=random.randrange(100),
            sys=random.randrange(100),
            iowait=random.randrange(100),
            irq=random.randrange(100),
            soft=random.randrange(100),
            steal=random.randrange(100),
            guest=random.randrange(100),
            gnice=random.randrange(100),
            idle=random.randrange(100),
        ).save()
