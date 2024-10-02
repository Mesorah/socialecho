from utils.base_for_tests.base_for_post import BaseCreatePost
from django.urls import reverse


class TestEditPostSocialEcho(BaseCreatePost):
    def test_if_request_is_post(self):
        response = self.client.post(
            reverse('social_echo:delete_post', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 302)
