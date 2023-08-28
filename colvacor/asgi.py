"""
ASGI config for colvacor project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colvacor.settings')

application = get_asgi_application()
#python manage.py inspectdb --database=nombre_basedatos --user=nombre_usuario --password=contraseña > models.py
#db_empresa
#python manage.py inspectdb --database=db_empresa --user=root --password=berdugo13 > models.py