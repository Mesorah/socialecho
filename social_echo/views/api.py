from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from social_echo.models import Posts
from social_echo.serializers import PostsSerializer


@api_view(http_method_names=['GET', 'POST'])
def post_api(request):
    if request.method == 'GET':
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def post_api_detail(request, pk):
    post = get_object_or_404(Posts, id=pk)

    if request.method == 'GET':
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PostsSerializer(
            instance=post,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
