from django.db import models
from django.contrib.auth.models import User


class AuthorUser(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                               related_name='authored_profiles')
    cover = models.ImageField(upload_to='media/user/%Y/%m/%d/',
                              blank=True, null=True,)
    follows = models.ManyToManyField(User, blank=True,
                                     related_name='followers')
    following = models.ManyToManyField(User, blank=True,
                                       related_name='following')

    def __str__(self):
        return f'{self.author}'
