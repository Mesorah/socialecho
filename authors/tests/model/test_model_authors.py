from django.test import TestCase
from authors.models import AuthorUser
from django.contrib.auth.models import User


class TestModelSocialEchol(TestCase):
    def test_post_retuns_correct_message(self):
        user = User.objects.create_user(username='Test', password='Test')
        author_user = AuthorUser.objects.create(author=user)

        self.assertEqual(str(author_user), 'Test')
