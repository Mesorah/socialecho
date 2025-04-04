from rest_framework.decorators import api_view
from rest_framework.response import Response

from social_echo.models import Posts
from social_echo.serializers import PostsSerializer


@api_view()
def post_api(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)

    return Response(serializer.data)


@api_view()
def post_api_detail(request, pk):
    posts = Posts.objects.filter(id=pk)
    serializer = PostsSerializer(posts, many=True)

    return Response(serializer.data)
