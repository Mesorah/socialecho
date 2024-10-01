from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoginAuthor(TestCase):
    def test_if_user_is_none(self):
        User.objects.create_user(username='JohnDoe', password='!@33dfDFG!2d')

        form_data = {
            'username': 'JaneDoe',
            'password': '!@33dfDFG!2d',
        }

        self.client.post(
            reverse('authors:login_author'), data=form_data)

        logout = self.client.post(reverse('authors:logout_author'), data=form_data)

        self.assertEqual(logout.status_code, 302)
