from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, AuthorUser
from .forms import CreatePost
from django.contrib.auth.decorators import login_required
from django.http import Http404


def home(request):
    posts = Posts.objects.all().order_by('-id')

    return render(request, 'social_echo/pages/home.html', context={
        'title': 'Home',
        'posts': posts
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            author_user = AuthorUser.objects.get(author=request.user)

            post.author_cover = author_user

            post.save()

            return redirect('social_echo:home')

    else:
        form = CreatePost()

    return render(request, 'global/pages/base_form.html', context={
        'form': form,
    })


@login_required
def edit_post(request, id):
    post = get_object_or_404(Posts, id=id)

    username = request.user
    is_user = Posts.objects.filter(author=username, id=id)

    if is_user:

        if request.method == 'POST':
            form = CreatePost(request.POST, request.FILES, instance=post)

            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user

                author_user = AuthorUser.objects.get(author=request.user)

                post.author_cover = author_user

                post.save()

                return redirect('social_echo:home')

        else:
            form = CreatePost(instance=post)
    else:
        raise Http404()

    return render(request, 'global/pages/base_form.html', context={
        'form': form,
    })


@login_required
def delete_post(request, id):
    post = get_object_or_404(Posts, id=id)

    post.delete()

    return redirect('social_echo:home')


def view_post(request, id):
    posts = get_object_or_404(Posts, id=id)

    if not posts.cover:
        raise Http404()

    return render(request, 'social_echo/pages/view_page.html', context={
        'title': 'View Page',
        'posts': posts
    })
