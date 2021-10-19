"""
ASGI config for django_chat_channels_redis project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

# When importing chat.routing, django needs to be already setup.
import django
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_chat_channels_redis.settings')

import chat.routing
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
