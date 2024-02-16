"""
WSGI config for my_django_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application



import sys

print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)
print("This message will appear in the Heroku logs", file=sys.stdout)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_portfolio.settings")

application = get_wsgi_application()
