from django.test import TestCase
from django.urls import reverse
from authors.models import AuthorUser


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

        self.assertIn('Register', response)

    def test_register_author_is_post(self):
        form_data = {
            'username': 'JaneDoe',
            'first_name': 'Jane',
            'last_name': 'Doeny',
            'email': 'jane.doe@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
        }

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)

        self.assertEqual(response.status_code, 302)

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

    def test_if_cover_is_not_none(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'JohnDoe',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
            'cover': '\\media\\2024\\09\29\\test_img.jpg'
        }

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)

        self.assertEqual(response.status_code, 302)

    def test_if_cover_is_none(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'JohnDoe',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
            'cover': ''
        }

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)

        self.assertEqual(response.status_code, 302)

    def test_cover_is_provided(self):
        cover_file_path = 'media\\media\\user\\base\\base_cover.jpeg'
        with open(cover_file_path, 'rb') as cover_file:
            form_data = {
                'first_name': 'Jane',
                'last_name': 'Doe',
                'username': 'JaneDoe',
                'email': 'jane.doe@example.com',
                'password': '!@33dfDFG!2d',
                'repeat_password': '!@33dfDFG!2d',
                'cover': cover_file
            }

            response = self.client.post(reverse('authors:register_author'),
                                        data=form_data)

            author_user = AuthorUser.objects.get(author__username='JaneDoe')

            self.assertTrue('base_cover' in author_user.cover.name and author_user.cover.name.endswith('.jpeg'), # noqa E501
                        f"Expected cover name to include 'base_cover' and end with '.jpeg', got: {author_user.cover.name}") # noqa E501

            self.assertEqual(response.status_code, 302)
