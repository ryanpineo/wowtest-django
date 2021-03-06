"""
WSGI config for ophelia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wowtest.settings")

import pymysql
pymysql.install_as_MySQLdb()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
