from rest_framework import serializers

from authors.models import AuthorUser
from social_echo.models import Posts


class AuthorSerializer(serializers.ModelSerializer):
    follows = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='username'
    )

    class Meta:
        model = AuthorUser
        fields = [
            'cover', 'follows', 'following'
        ]


class PostsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(read_only=True)
    author_user = AuthorSerializer(
        source='author_cover', read_only=True
    )

    class Meta:
        model = Posts
        fields = [
            'id', 'title', 'message',
            'cover', 'author', 'author_user'
        ]
