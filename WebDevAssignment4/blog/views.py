# from rest_framework import viewsets, mixins
# from rest_framework.permissions import IsAuthenticated
# from .models import Post, Comment
# from .serializers import PostSerializer, CommentSerializer
# from .permissions import IsAuthorOrReadOnly

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# class CommentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

#     def get_queryset(self):
#         post_id = self.kwargs.get('post_id')
#         if post_id is None:
#             return Comment.objects.none()
#         return self.queryset.filter(post_id=post_id)

#     def perform_create(self, serializer):
#         post_id = self.kwargs.get('post_id')
#         serializer.save(post_id=post_id, author=self.request.user)

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

# # Task 2.3 start
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

# def perform_create(self, serializer):
#     comment = serializer.save(author=self.request.user)
#     channel_layer = get_channel_layer()
#     group_name = f'post_{comment.post.id}'

#     async_to_sync(channel_layer.group_send)(
#         group_name,
#         {
#             'type': 'send_comment_notification',
#             'comment': {
#                 'id': comment.id,
#                 'author': comment.author.username,
#                 'content': comment.content,
#                 'timestamp': comment.timestamp.isoformat(),
#             }
#         }
#     )
# # Task 2.3 end

class PostPagination(PageNumberPagination):
    page_size = 5


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    permission_classes = [AllowAny]  # No authentication required for Exercise 2
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id is None:
            return Comment.objects.none()
        return self.queryset.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(post_id=post_id, author=self.request.user)
