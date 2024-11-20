from utils.base_for_tests.base_for_post import BaseCreatePost
from django.urls import reverse
import pytest


@pytest.mark.part
class TestDashboardSocialEcho(BaseCreatePost):
    def test_dashboard_returns_200(self):

        response = self.client.get(
            reverse('dashboard:home', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)

    def test_dashboard_returns_404(self):

        response = self.client.get(
            reverse('dashboard:home', kwargs={'id': 11}))

        self.assertEqual(response.status_code, 404)

    def test_if_dashboard_returns_correct_template(self):

        response = self.client.get(
            reverse('dashboard:home', kwargs={'id': 1}))

        self.assertTemplateUsed(response, 'dashboard/pages/dashboard.html')

    def test_if_user_is_none_but_dashboard_exists(self):
        # self.client.logout() ja está deslogado(nao sei o porque)

        response = self.client.get(
            reverse('dashboard:home', kwargs={'id': 1}))

        self.assertEqual(response.status_code, 200)

    def test_dashboard_follows(self):
        response = self.client.get(
            reverse('dashboard:home', kwargs={'id': 1}))

        self.assertIn('follows', response.context)

        self.assertEqual(response.context['follows'], 0)

        self.assertContains(response, 'Seguidores: 0')

    def test_dashboard_following(self):
        response = self.client.get(
            reverse('dashboard:home', kwargs={'id': 1}))

        self.assertIn('following', response.context)

        self.assertEqual(response.context['following'], 0)

        self.assertContains(response, 'Seguindo: 0')

# trazer a classe para cima por: self.create_user direto


# @pytest.mark.part
# class TestDashboardFFSocialEcho(BaseLoginAuthor):
#     def setUp(self):
#         self.new_author = self.create_user()

#         self.author = AuthorUser()
#         self.author.author = self.author_user.author
#         self.author.save()

#         self.author.follows.add(self.new_author)
#         self.author.following.add(self.new_author)

#         return super().setUp()

#     def test_dashboard_follows_is_not_zero(self):
#         self.assertEqual(self.author.follows.count(), 1)

#     def test_dashboard_following_is_not_zero(self):
#         self.assertEqual(self.author.following.count(), 1)
