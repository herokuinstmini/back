from instmini.serializers import PostSerializer, TagSerializer
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from .custom_renderers import *
from .models import Post, Tag
from .serializers import *


class ImageAPIView(generics.RetrieveAPIView):

    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpg')


class TagListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = Post.objects.filter(tags__name=tag)
            return queryset
        return Post.objects.all()


class UsersPostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        # pk = int(self.kwargs['pk'])
        # return Post.objects.filter(author__id=pk)
        username = self.kwargs['username']
        return Post.objects.filter(author__username=username)
