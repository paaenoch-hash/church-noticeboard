import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import noticeboard.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noticeboard.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            noticeboard.routing.websocket_urlpatterns
        )
    ),
})