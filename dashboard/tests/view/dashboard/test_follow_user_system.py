from utils.base_for_tests.base_for_post import BaseCreatePost
from django.urls import reverse
import pytest


@pytest.mark.part
class TestFollowUserSystem(BaseCreatePost):
    def setUp(self):
        self.create_user()

        return super().setUp()

    def test_follow_user(self):
        response = self.client.get(
            reverse('dashboard:follow_user_system', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 302)
