"""Plantilla de `manage.py` — sustituir por el generado por `django-admin startproject`.

No ejecutar este archivo directamente; sirve como referencia para la estructura.
"""

import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluaciones__nombre__estudiantes.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
