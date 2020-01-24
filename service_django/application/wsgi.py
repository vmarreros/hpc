#!/usr/bin/env python
from os import environ
from django.core.wsgi import get_wsgi_application

environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.%s' % (environ.get('ENVIRONMENT'),))
application = get_wsgi_application()
