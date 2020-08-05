"""
WSGI config for blog2020 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog2020.settings")
profile = os.environ.get('BLOG2020_PROFILE', 'develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog2020.settings.%s" % profile)

application = get_wsgi_application()
