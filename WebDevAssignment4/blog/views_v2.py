from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers_v2 import PostSerializerV2

class PostViewSetV2(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerV2