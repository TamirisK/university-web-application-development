from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import profile_view

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Authentication Views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Blog App URLs
    path('', include('blog.urls')),

    # User Profile Views
    path('accounts/profile/', profile_view, name='profile'),
]
