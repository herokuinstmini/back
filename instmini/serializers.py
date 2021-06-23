from rest_framework import fields, serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(
        source='author', read_only=True)
    tag_names = serializers.StringRelatedField(
        source='tags', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_name', 'tags', 'tag_names', 'image']
