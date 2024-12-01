from rest_framework import serializers
from .models import Post, Comment

class CommentSerializerV2(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'timestamp']

class PostSerializerV2(serializers.ModelSerializer):
    comments = CommentSerializerV2(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'timestamp', 'comments', 'status']