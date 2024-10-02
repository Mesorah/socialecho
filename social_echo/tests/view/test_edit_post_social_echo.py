from utils.base_for_tests.base_for_post import BaseCreatePost
from utils.base_for_tests.base_for_login import BaseLoginAuthor
from django.urls import reverse


class TestEditPostSocialEcho(BaseCreatePost):
    def setUp(self) -> None:
        self.form_data = {
            'title': 'I am a test title2',
            'message': 'I am a test message2',
        }

        return super().setUp()

    def test_if_request_is_get(self):
        response = self.client.get(
            reverse('social_echo:edit_post', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)

    def test_if_request_is_post(self):
        response = self.client.get(
            reverse('social_echo:edit_post', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)

    def test_if_post_is_valid(self):
        response = self.client.post(
            reverse('social_echo:edit_post', kwargs={'id': 1}),
            data=self.form_data)

        self.assertEqual(response.status_code, 302)

    def test_if_post_is_not_valid(self):
        self.form_data['title'] = {}

        response = self.client.post(
            reverse('social_echo:edit_post', kwargs={'id': 1}),
            data=self.form_data)

        self.assertEqual(response.status_code, 200)

    def test_if_the_post_is_not_the_user(self):
        BaseLoginAuthor.create_user(
            self,
            username='Testing2',
            password='test2',
        )

        BaseCreatePost.create_post(self)

        response = self.client.post(
            reverse('social_echo:edit_post', kwargs={'id': 1}),
            data=self.form_data)

        self.assertEqual(response.status_code, 404)
