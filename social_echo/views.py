from django.shortcuts import render
from .models import Posts


def home(request):
    posts = Posts.objects.all()

    return render(request, 'social_echo/pages/home.html', context={
        'title': 'Home',
        'posts': posts
    })
