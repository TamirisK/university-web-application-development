import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from blog.routing import websocket_urlpatterns  # Import the routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # WebSocket protocol
        URLRouter(
            websocket_urlpatterns  # WebSocket routing
        )
    ),
})