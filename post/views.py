from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

# Create your views here.

# using Model ViewSet
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# Using Viewsets
class PostListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
