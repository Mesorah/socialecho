from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from authors.models import AuthorUser


class Posts(models.Model):
    title = models.CharField(max_length=55)
    message = models.CharField(max_length=155)
    cover = models.ImageField(upload_to='media/%Y/%m/%d/',
                              blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    author_cover = models.ForeignKey(
        AuthorUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.message}'

    def get_absolute_url(self):
        return reverse('social_echo:view_post', args=(self.id,))

    def get_edit_url(self):
        return reverse('social_echo:edit_post', args=(self.id,))

    def get_delete_url(self):
        return reverse('social_echo:delete_post', args=(self.id,))
