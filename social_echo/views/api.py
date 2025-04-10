from rest_framework.generics import (  # noqa E501
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from social_echo.models import Posts
from social_echo.serializers import PostSerializer


class PostAPIPagination(PageNumberPagination):
    page_size = 10


class PostAPIModelViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostAPIPagination


class PostAPIView(ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostAPIPagination


class PostAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
