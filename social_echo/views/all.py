from django.shortcuts import (
    render,
    get_object_or_404,
)
from social_echo.models import Posts
from django.views.generic import ListView
from django.http import Http404


class PostListView(ListView):
    model = Posts
    template_name = 'social_echo/pages/home.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostListViewHome(PostListView):
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.all().order_by('-id')

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Home',
        })

        return context


def home(request):
    posts = Posts.objects.all().order_by('-id')

    return render(request, 'social_echo/pages/home.html', context={
        'title': 'Home',
        'posts': posts
    })


def view_post(request, id):
    posts = get_object_or_404(Posts, id=id)

    if not posts.cover:
        raise Http404()

    return render(request, 'social_echo/pages/view_page.html', context={
        'title': 'View Page',
        'posts': posts
    })
