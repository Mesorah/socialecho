from django.test import TestCase
from django.contrib.auth.models import User
from authors.models import AuthorUser


class BaseLoginAuthor(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Testing',
            password='test',
        )

        self.client.login(username='Testing', password='test')

        self.user_instance = User.objects.get(username='Testing')

        self.author_user = AuthorUser()
        self.author_user.author = self.user_instance
        self.author_user.save()

        return super().setUp()

    def create_user(self, username='test2', password='test2'):
        self.user = User.objects.create_user(
            username=username,
            password=password
        )

        self.client.login(username=username, password=password)

        self.user_instance = User.objects.get(username=username)

        self.author_user = AuthorUser()
        self.author_user.author = self.user_instance
        self.author_user.save()

        self.author_user_author = self.author_user.author

        return self.author_user_author
