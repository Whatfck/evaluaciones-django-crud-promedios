"""WSGI config for evaluaciones__nombre__estudiantes."""

import os

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
from django.db import connections

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluaciones__nombre__estudiantes.settings')

application = get_wsgi_application()

if os.getenv('VERCEL'):
	connection = connections['default']
	database_name = str(connection.settings_dict['NAME'])
	if database_name.startswith('/tmp/'):
		call_command('migrate', interactive=False, run_syncdb=True, verbosity=0)
