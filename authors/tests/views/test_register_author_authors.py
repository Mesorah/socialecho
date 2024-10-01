from django.test import TestCase
from django.urls import reverse


class TestRegisterAuthor(TestCase):
    def test_register_author_returns_status_code_200(self):
        response = self.client.get(reverse('authors:register_author'))

        self.assertEqual(response.status_code, 200)

    def test_register_author_returns_correct_template(self):
        response = self.client.get(reverse('authors:register_author'))

        self.assertTemplateUsed(response, 'global/pages/base_form.html')

    def test_register_author_returns_correct_word(self):
        response = self.client.get(reverse(
            'authors:register_author')).content.decode('utf-8')

        self.assertIn('<h1>Social Echo</h1>', response)

    def test_register_author_is_post(self):
        response = self.client.post(reverse('authors:register_author'))

        self.assertEqual(response.status_code, 200)

    def test_if_form_is_not_valid(self):
        form_data = {
            'username': 'a',
            'password': 'av',
            'repeat_password': 'add',
        }

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)

        self.assertEqual(response.status_code, 200)

        form = response.context['form']
        self.assertFalse(form.is_valid())

    def test_if_form_is_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'JohnDoe',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
        }

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)

        self.assertEqual(response.status_code, 302)
