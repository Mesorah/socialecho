from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.CharField(max_length=55)
    message = models.CharField(max_length=155)
    cover = models.ImageField(upload_to='media/%Y/%m/%d/',
                              blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.message}'
