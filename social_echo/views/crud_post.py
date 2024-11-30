from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from social_echo.models import Posts, AuthorUser
from social_echo.forms import CreatePost
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


@method_decorator(
    login_required(login_url='authors:login_author',
                   redirect_field_name='next'
                   ),
    name='dispatch'
)
class PostCreateView(CreateView):
    template_name = 'global/pages/base_form.html'
    model = Posts
    success_url = reverse_lazy('social_echo:home')
    form_class = CreatePost

    def form_valid(self, form):
        form.instance.author = self.request.user

        try:
            author_user = AuthorUser.objects.get(author=self.request.user)
        except AuthorUser.DoesNotExist:
            author_user = None

        if author_user:
            form.instance.author_cover = author_user

        return super().form_valid(form)


@method_decorator(
    login_required(login_url='authors:login_author',
                   redirect_field_name='next'
                   ),
    name='dispatch'
)
class PostUpdateView(UpdateView):
    template_name = 'global/pages/base_form.html'
    model = Posts
    success_url = reverse_lazy('social_echo:home')
    form_class = CreatePost

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.author != self.request.user:
            raise Http404()

        return obj


@method_decorator(
    login_required(login_url='authors:login_author',
                   redirect_field_name='next'
                   ),
    name='dispatch'
)
class PostDeleteView(DeleteView):
    template_name = None
    model = Posts
    success_url = reverse_lazy('social_echo:home')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.author != self.request.user:
            raise Http404()

        return obj

    def get(self, request, *args, **kwargs):
        # só pra ter certeza que ninguém irá
        # excluir como get

        raise Http404()
