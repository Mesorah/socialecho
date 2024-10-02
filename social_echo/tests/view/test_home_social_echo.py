from django.test import TestCase
from django.urls import reverse


class TestHomeSocialEcho(TestCase):
    def test_home_returns_status_code_200(self):
        response = self.client.get(reverse('social_echo:home'))

        self.assertEqual(response.status_code, 200)

    def test_home_returns_correct_template(self):
        response = self.client.get(reverse('social_echo:home'))

        self.assertTemplateUsed(response, 'social_echo/pages/home.html')

    def test_home_returns_correct_word(self):
        response = self.client.get(reverse(
            'social_echo:home')).content.decode('utf-8')

        self.assertIn('Social Echo', response)
