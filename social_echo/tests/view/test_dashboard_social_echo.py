from utils.base_for_tests.base_for_post import BaseLoginAuthor
from django.urls import reverse


class TestDashboardSocialEcho(BaseLoginAuthor):
    def test_dashboard_returns_200(self):

        response = self.client.get(
            reverse('social_echo:dashboard'))

        self.assertEqual(response.status_code, 200)

    def test_if_dashboard_returns_correct_template(self):

        response = self.client.get(
            reverse('social_echo:dashboard'))

        self.assertTemplateUsed(response, 'social_echo/pages/dashboard.html')
