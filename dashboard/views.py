from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from .models import Posts, AuthorUser
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User


def dashboard(request, id):
    posts = Posts.objects.filter(author=id)

    author = AuthorUser.objects.filter(author=id).first()

    you = AuthorUser.objects.filter(author=request.user).first()

    user_followings = you.following.all()

    user = None

    if not posts:
        raise Http404()
    else:
        user = posts[0].author

    try:
        cover = author.cover
        follows = author.follows.count()
        following = author.following.count()

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
        'user_followings': user_followings
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


@login_required
def follow_user_system(request, id):
    author = get_object_or_404(AuthorUser, author=request.user)
    author_for_follow = get_object_or_404(AuthorUser, id=id)

    author.following.add(author_for_follow.author)
    author_for_follow.follows.add(author.author)

    return redirect('social_echo:dashboard', id=id)


@login_required
def unfollow_user_system(request, id):
    author = get_object_or_404(AuthorUser, author=request.user)
    author_for_follow = get_object_or_404(AuthorUser, id=id)

    author.following.remove(author_for_follow.author)
    author_for_follow.follows.remove(author.author)

    return redirect('social_echo:dashboard', id=id)
