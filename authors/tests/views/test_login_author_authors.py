from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestLoginAuthor(TestCase):
    def test_login_author_returns_status_code_200(self):
        response = self.client.get(reverse('authors:login_author'))

        self.assertEqual(response.status_code, 200)

    def test_login_author_returns_correct_template(self):
        response = self.client.get(reverse('authors:login_author'))

        self.assertTemplateUsed(response, 'global/pages/base_form.html')

    def test_login_author_returns_correct_word(self):
        response = self.client.get(reverse(
            'authors:login_author')).content.decode('utf-8')

        self.assertIn('Login', response)

    def test_login_author_is_post(self):
        response = self.client.post(reverse('authors:login_author'))

        self.assertEqual(response.status_code, 200)

    def test_if_form_is_not_valid(self):
        form_data = {
            'username': '',
            'password': '',
        }

        response = self.client.post(
            reverse('authors:login_author'), data=form_data)

        self.assertEqual(response.status_code, 200)

        form = response.context['form']
        self.assertFalse(form.is_valid())

    def test_if_form_is_valid(self):
        User.objects.create_user(username='JohnDoe', password='!@33dfDFG!2d')

        form_data = {
            'username': 'JohnDoe',
            'password': '!@33dfDFG!2d',
        }

        response = self.client.post(
            reverse('authors:login_author'), data=form_data)

        self.assertEqual(response.status_code, 302)

    def test_if_user_is_none(self):
        User.objects.create_user(username='JohnDoe', password='!@33dfDFG!2d')

        form_data = {
            'username': 'JaneDoe',
            'password': '!@33dfDFG!2d',
        }

        response = self.client.post(
            reverse('authors:login_author'), data=form_data)

        self.assertEqual(response.status_code, 200)
