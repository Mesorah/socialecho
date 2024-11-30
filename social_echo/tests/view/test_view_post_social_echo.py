from utils.base_for_tests.base_for_post import BaseCreatePost
from django.urls import reverse


class TestViewPostSocialEcho(BaseCreatePost):
    def test_if_view_post_returns_200(self):
        self.create_post()

        response = self.client.get(
            reverse('social_echo:view_post', kwargs={'pk': 2}))

        self.assertEqual(response.status_code, 200)

    def test_if_view_post_returns_correct_template(self):
        self.create_post()

        response = self.client.get(
            reverse('social_echo:view_post', kwargs={'pk': 2}))

        self.assertTemplateUsed(response, 'social_echo/pages/view_page.html')
