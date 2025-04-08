from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from social_echo.models import Posts
from social_echo.serializers import PostsSerializer


class PostApiView(APIView):
    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)

        serializer = PostsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class PostApiDetailView(APIView):
    def get_post(self, pk):
        return get_object_or_404(Posts, id=pk)

    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = PostsSerializer(post)

        return Response(serializer.data)

    def patch(self, request, pk):
        post = self.get_post(pk)
        serializer = PostsSerializer(
            instance=post,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        post = self.get_post(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
