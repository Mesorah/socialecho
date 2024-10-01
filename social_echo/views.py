from django.shortcuts import render, redirect
from .models import Posts, AuthorUser
from .forms import CreatePost


def home(request):
    posts = Posts.objects.all().order_by('-id')

    return render(request, 'social_echo/pages/home.html', context={
        'title': 'Home',
        'posts': posts
    })


def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            try:
                author_user = AuthorUser.objects.get(author=request.user)
                post.author_cover = author_user
            except AuthorUser.DoesNotExist:
                post.author_cover = request.user

            post.save()

            return redirect('social_echo:home')

    else:
        form = CreatePost()

    return render(request, 'global/pages/base_form.html', context={
        'form': form,
    })
