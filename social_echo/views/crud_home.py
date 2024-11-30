from social_echo.models import Posts
from django.views.generic import ListView, DetailView


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


class ViewPostDetailView(DetailView):
    template_name = 'social_echo/pages/view_page.html'
    model = Posts
    context_object_name = 'post'
