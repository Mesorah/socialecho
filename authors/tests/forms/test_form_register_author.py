from django.test import TestCase
from django.urls import reverse
# from authors.forms import RegisterAuthor


class TestRegisterAuthorForm(TestCase):
    def setUp(self):
        self.form_data = {
            'username': 'JohnDoe',
            'first_name': 'Johny',
            'last_name': 'Doeny',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
        }

        self.client.post(
            reverse('authors:register_author'), data=self.form_data)

        super().setUp()

    def test_email_is_duplicate(self):
        self.form_data['username'] = 'JaneDoe'
        self.form_data['first_name'] = 'Jane'
        self.form_data['last_name'] = 'Doeny'

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)

        self.assertEqual(response.status_code, 200)

    def test_email_is_not_duplicate(self):
        self.form_data['username'] = 'JaneDoe'
        self.form_data['first_name'] = 'Jane'
        self.form_data['last_name'] = 'Doeny'
        self.form_data['email'] = 'jane.doe@example.com'

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)

        self.assertEqual(response.status_code, 302)

    def test_user_is_duplicate(self):
        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)

        self.assertEqual(response.status_code, 200)

    def test_user_is_not_duplicate(self):
        form_data = {
            'username': 'Test',
            'first_name': 'Johny',
            'last_name': 'Doeny',
            'email': 'test@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
        }

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)

        self.assertEqual(response.status_code, 302)

    def test_the_invalid_password(self):
        self.form_data['password'] = '1'
        self.form_data['repeat_password'] = '1'

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)

        self.assertEqual(response.status_code, 200)
