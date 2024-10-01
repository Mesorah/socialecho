from django.test import TestCase
from django.urls import reverse
# from authors.forms import RegisterAuthor


class TestRegisterAuthorForm(TestCase):
    def setUp(self):
        super().setUp()  # Remover o return aqui
        self.form_data = {
            'username': 'JohnDoe',
            'first_name': 'Johny',
            'last_name': 'Doeny',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
        }

    def test_if_username_and_email_exists(self):
        # Cria o autor
        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 302)

        # Tenta registrar novamente com o mesmo username e email
        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 200)

        # Verifica se as mensagens de erro estão presentes
        self.assertContains(response, 'este e-mail já existe')
        self.assertContains(response, 'esse username já existe')

    def test_if_username_and_email_not_exists(self):
        form_data = {
            'username': 'JaneDoe',
            'first_name': 'Jane',
            'last_name': 'Doeny',
            'email': 'jane.doe@example.com',
            'password': '!@33dfDFG!2d',
            'repeat_password': '!@33dfDFG!2d',
        }

        # Primeiro registro, deve ser bem-sucedido
        response = self.client.post(
            reverse('authors:register_author'), data=form_data)
        self.assertEqual(response.status_code, 302)

        # Teste com novos dados que não existem
        form_data['username'] = 'Testing'
        form_data['first_name'] = 'Test'
        form_data['last_name'] = 'Test'
        form_data['email'] = 'testing@example.com'

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)
        self.assertEqual(response.status_code, 302)
