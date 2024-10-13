from utils.base_for_tests.base_for_post import BaseCreatePost
from social_echo.models import AuthorUser
from django.urls import reverse


class TestDashboardListFollowsSocialEcho(BaseCreatePost):
    def test_dashboard_follows_returns_200(self):
        response = self.client.get(
            reverse('social_echo:list_follows', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)

    def test_dashboard_follows_returns_404(self):
        response = self.client.get(
            reverse('social_echo:list_follows', kwargs={'id': 2}))

        self.assertEqual(response.status_code, 404)

    def test_if_follows_user_is_not_equal_to_author(self):
        self.new_author = self.create_user()

        self.author = AuthorUser()
        self.author.author = self.author_user.author
        self.author.save()

        response = self.client.get(
            reverse('social_echo:list_follows', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['type_'], 'follows')

    def test_if_type_is_not_cert(self):
        self.new_author = self.create_user()

        self.author = AuthorUser()
        self.author.author = self.author_user.author
        self.author.save()

        response = self.client.get(
            reverse('social_echo:list_follows', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['type_'], 'following')


class TestDashboardListFollowingSocialEcho(BaseCreatePost):
    def test_dashboard_following_returns_200(self):
        response = self.client.get(
            reverse('social_echo:list_following', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)

    def test_dashboard_following_returns_404(self):
        response = self.client.get(
            reverse('social_echo:list_following', kwargs={'id': 2}))

        self.assertEqual(response.status_code, 404)

    def test_if_following_user_is_not_equal_to_author(self):
        self.new_author = self.create_user()

        self.author = AuthorUser()
        self.author.author = self.author_user.author
        self.author.save()

        response = self.client.get(
            reverse('social_echo:list_following', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['type_'], 'following')

    def test_if_type_is_not_cert(self):
        self.new_author = self.create_user()

        self.author = AuthorUser()
        self.author.author = self.author_user.author
        self.author.save()

        response = self.client.get(
            reverse('social_echo:list_follows', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['type_'], 'follow')
