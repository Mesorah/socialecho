from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from .models import Posts, AuthorUser
from .forms import CreatePost
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User


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


def dashboard(request, id):
    posts = Posts.objects.filter(author=id)

    user = None

    if not posts:
        raise Http404()
    else:
        user = posts[0].author

    try:
        cover = posts[0].author_cover.cover
        follows = posts[0].author_cover.follows.count()
        following = posts[0].author_cover.following.count()
    except AttributeError:
        cover = 'media/user/base/base_cover.jpeg'
        follows = 0
        following = 0

    return render(request, 'social_echo/pages/dashboard.html', context={
        'posts': posts,
        'user': user,
        'cover': cover,
        'follows': follows,
        'following': following,
    })


def list_follows_or_following(request, id, type_):
    author = get_object_or_404(AuthorUser, id=id)

    owner = False

    if str(request.user) == str(author):
        owner = True

    if type_ == 'follows':
        users = author.follows.all()
    elif type_ == 'following':
        users = author.following.all()

    return render(request, 'social_echo/pages/list_follows_following.html', context={ # noqa E501
        'users': users,
        'owner': owner,
        'type_': type_,
    })


@login_required
def unfollow_or_unfollowing(request, id, type_):
    # Deixar só como post
    author = AuthorUser.objects.filter(author=request.user).first()

    unfollow_user = get_object_or_404(User, id=id)

    if type_ == 'unfollow':
        if unfollow_user in author.follows.all():
            author.follows.remove(unfollow_user)

    elif type_ == 'unfollowing':
        if unfollow_user in author.following.all():
            author.following.remove(unfollow_user)

    return redirect('social_echo:home')
