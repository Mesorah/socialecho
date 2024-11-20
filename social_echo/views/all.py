from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from social_echo.models import Posts
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import Http404


class PostListView(ListView):
    model = Posts
    template_name = 'social_echo/pages/home.html'
    context_object_name = 'posts'
    paginate_by = 5


def home(request):
    posts = Posts.objects.all().order_by('-id')

    return render(request, 'social_echo/pages/home.html', context={
        'title': 'Home',
        'posts': posts
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
