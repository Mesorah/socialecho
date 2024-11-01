from utils.base_for_tests.base_for_post import BaseCreatePost
from social_echo.models import AuthorUser
from django.urls import reverse
import pytest


@pytest.mark.part
class TestDashboardUnlistFollowsSocialEcho(BaseCreatePost):
    def test_dashboard_unfollows_returns_302(self):
        response = self.client.get(
            reverse('dashboard:unfollow_user', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 302)

    def test_dashboard_unfollows_returns_404(self):
        response = self.client.get(
            reverse('dashboard:unfollow_user', kwargs={'id': 2}))

        self.assertEqual(response.status_code, 404)

    def test_if_unfollow_user_in_author_follow(self):
        self.new_author = self.create_user()

        self.author = AuthorUser()
        self.author.author = self.author_user.author
        self.author.save()

        response = self.client.get(
            reverse('dashboard:unfollow_user', kwargs={'id': 2}))

        self.assertEqual(response.status_code, 302)

    def test_if_unfollow_user_not_in_author_follow(self):
        self.new_author = self.create_user()

        self.author = AuthorUser()
        self.author.author = self.author_user.author
        self.author.save()

        response = self.client.get(
            reverse('dashboard:unfollow_user', kwargs={'id': 3}))

        self.assertEqual(response.status_code, 404)


@pytest.mark.part
class TestDashboardUnlistFollowingSocialEcho(BaseCreatePost):
    def test_dashboard_unfollowing_returns_302(self):
        response = self.client.get(
            reverse('dashboard:unfollowing_user', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 302)

    def test_dashboard_unfollowing_returns_404(self):
        response = self.client.get(
            reverse('dashboard:unfollowing_user', kwargs={'id': 2}))

        self.assertEqual(response.status_code, 404)
