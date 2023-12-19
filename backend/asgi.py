"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from home.consumers import TestConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

ws_patterns = [
    path('test/', TestConsumer.as_asgi())
]
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': URLRouter(ws_patterns)
})
