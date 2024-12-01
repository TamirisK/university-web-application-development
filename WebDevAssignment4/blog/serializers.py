# from rest_framework import serializers
# from .models import Post, Comment
# from rest_framework.fields import CurrentUserDefault

# class CommentSerializer(serializers.ModelSerializer):
#   author = serializers.ReadOnlyField(source='author.username')

#   class Meta:
#     model = Comment
#     fields = ['id', 'post', 'author', 'content', 'timestamp']
#     read_only_fields = ['id', 'timestamp']

#   def create(self, validated_data):
#     validated_data['author'] = self.context['request'].user
#     return super().create(validated_data)

#   def update(self, instance, validated_data):
#     validated_data.pop('author', None)
#     return super().update(instance, validated_data)
  
# class PostSerializer(serializers.ModelSerializer):
#   comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  
#   class Meta:
#     model = Post
#     fields = ['id', 'title', 'content', 'author', 'timestamp', 'comments', 'status']
#     read_only_fields = ['id', 'timestamp']

#   def create(self, validated_data):
#     validated_data['author'] = self.context['request'].user
#     return super().create(validated_data)

#   def update(self, instance, validated_data):
#     validated_data.pop('author', None)
#     return super().update(instance, validated_data)


# Exercise 2
from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_name', 'content', 'timestamp']
        read_only_fields = ['id', 'timestamp', 'author_name']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'timestamp', 'comments', 'status']
        read_only_fields = ['id', 'timestamp']
