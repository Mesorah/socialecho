from django.test import TestCase
from social_echo.models import Posts
from django.contrib.auth.models import User


class TestModelSocialEchol(TestCase):
    def test_post_retuns_correct_message(self):
        user = User.objects.create_user(username='Test', password='Test')
        message = 'I am a test'
        post = Posts.objects.create(
            title='test', message=message, author=user)

        self.assertEqual(str(post), 'I am a test')
