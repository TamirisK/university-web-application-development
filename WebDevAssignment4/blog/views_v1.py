from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers_v1 import PostSerializerV1
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class PostViewSetV1(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerV1
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Apply throttling to this view