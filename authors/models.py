from django.db import models
from django.contrib.auth.models import User


class AuthorUser(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='media/user/%Y/%m/%d/',
                              blank=True, null=True,
                              default='media/user/base/base_cover.jpeg')

    def __str__(self):
        return f'{self.author}'
