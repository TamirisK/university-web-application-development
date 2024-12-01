from django.urls import path
from .consumers import CommentNotificationConsumer

websocket_urlpatterns = [
    path('ws/posts/<int:post_id>/', CommentNotificationConsumer.as_asgi()),
]