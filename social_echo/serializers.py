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


class PostSerializer(serializers.ModelSerializer):
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

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                'Título precisa ser maior que 3 caracteres'
            )

        return value

    def validate(self, attrs):
        super_validate = super().validate(attrs)

        title = attrs.get('title')
        message = attrs.get('message')

        if title == message:
            raise serializers.ValidationError(
                'O título e a mensagem não pode ser iguais'
            )

        return super_validate
