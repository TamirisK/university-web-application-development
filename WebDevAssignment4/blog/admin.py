from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'timestamp', 'status')
  list_filter = ('status', 'timestamp', 'author')
  search_fields = ('title', 'content')
  ordering = ('-timestamp',)
  prepopulated_fields = {'title': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('post', 'author', 'timestamp')
  list_filter = ('timestamp', 'author')
  search_fields = ('content',)