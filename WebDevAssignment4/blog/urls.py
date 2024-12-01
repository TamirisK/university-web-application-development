from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views_v1 import PostViewSetV1
from .views_v2 import PostViewSetV2


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Routers for version 1
router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSetV1, basename='post_v1')

# Routers for version 2
router_v2 = DefaultRouter()
router_v2.register(r'posts', PostViewSetV2, basename='post_v2')

urlpatterns = [
    path('', include(router.urls)),

    path('v1/', include((router_v1.urls, 'v1'), namespace='v1')),
    path('v2/', include((router_v2.urls, 'v2'), namespace='v2')),

    path('posts/<int:post_id>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='post-comments'),
]