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
        self.assertNotEqual(response.context['type_'], 'following')

    def test_if_follows_user_is_equal_to_author(self):
        response = self.client.get(
            reverse('social_echo:list_follows',
                    kwargs={'id': self.author_user.author.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['owner'])

    def test_follows_template_used(self):
        response = self.client.get(
            reverse('social_echo:list_follows', kwargs={'id': 1}))

        self.assertTemplateUsed(response,
                                'social_echo/pages/list_follows_following.html'
                                )

    def test_follows_view_for_anonymous_user(self):
        self.client.logout()

        response = self.client.get(
            reverse('social_echo:list_follows', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['owner'])

    def test_follows_users_in_context(self):
        response = self.client.get(
            reverse('social_echo:list_follows',
                    kwargs={'id': self.author_user.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['users']),
                         list(self.author_user.follows.all()))


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
        self.assertNotEqual(response.context['type_'], 'follows')

    def test_if_following_user_is_equal_to_author(self):
        response = self.client.get(
            reverse('social_echo:list_following',
                    kwargs={'id': self.author_user.author.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['owner'])

    def test_following_template_used(self):
        response = self.client.get(
            reverse('social_echo:list_following', kwargs={'id': 1}))

        self.assertTemplateUsed(response,
                                'social_echo/pages/list_follows_following.html'
                                )

    def test_following_view_for_anonymous_user(self):
        self.client.logout()

        response = self.client.get(
            reverse('social_echo:list_following', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['owner'])

    def test_following_users_in_context(self):
        response = self.client.get(
            reverse('social_echo:list_following',
                    kwargs={'id': self.author_user.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['users']),
                         list(self.author_user.following.all()))

    def test_cover(self):
        self.post.cover = ''

        response = self.client.get(
            reverse('social_echo:list_following',
                    kwargs={'id': self.author_user.id}))

        self.assertEqual(response.status_code, 200)
