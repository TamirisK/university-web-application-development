from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    add_comment, edit_comment, edit_profile
)

urlpatterns = [
    # Post-related Views
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment-related Views
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),

    # User Profile Views
    path('accounts/profile/', edit_profile, name='profile'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

