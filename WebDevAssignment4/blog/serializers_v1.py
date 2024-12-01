from rest_framework import serializers
from .models import Post, Comment

class CommentSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'timestamp']

class PostSerializerV1(serializers.ModelSerializer):
    comments = CommentSerializerV1(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'timestamp', 'comments', 'status']