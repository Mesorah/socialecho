from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from social_echo.models import Posts
from social_echo.serializers import PostSerializer


class PostAPIPagination(PageNumberPagination):
    page_size = 10


class PostAPIModelViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostAPIPagination
    permission_classes = [IsAuthenticated,]
