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


@api_view(http_method_names=['GET'])
def post_api_detail(request, pk):
    if request.method == 'GET':
        post = Posts.objects.filter(id=pk)
        serializer = PostsSerializer(post, many=True)
        return Response(serializer.data)
