"""Plantilla de `settings.py` para referencia del equipo.

Rellenar valores reales al crear el proyecto. Esto NO es una configuración completa,
solo sirve como guía y puntos clave a verificar.
"""

import os

# TODO: completar con valores reales al crear el proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'replace-me'
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Añadir la app de calificaciones aquí
    # 'calificaciones_nombre__estudiantes',
]

# Resto de configuración: DATABASES, TEMPLATES, STATIC_URL, etc.
