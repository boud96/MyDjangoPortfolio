"""
WSGI config for my_django_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_portfolio.settings")

print("BRUH")
print()
print()
print()
print()
print()
print(os.environ.get('DJANGO_SETTINGS_MODULE'))

application = get_wsgi_application()

print("Python paths:")