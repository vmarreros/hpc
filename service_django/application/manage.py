#!/usr/bin/env python
from os import environ
from sys import argv
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.%s' % (environ.get('ENVIRONMENT'), ))
    execute_from_command_line(argv)
