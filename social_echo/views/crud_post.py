from django.views import View
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from social_echo.models import Posts, AuthorUser
from social_echo.forms import CreatePost
from django.http import Http404


@method_decorator(
    login_required(login_url='authors:login_author',
                   redirect_field_name='next'
                   ),
    name='dispatch'
)
class PostCreateUpdateView(View):
    def get_post(self, id):
        post = None

        if id is not None:
            post = get_object_or_404(Posts, id=id)

            if not post:
                raise Http404()

        return post

    def render_post(self, form):
        return render(self.request, 'global/pages/base_form.html', context={
            'form': form,
        })

    def get(self, request, id=None):
        post = self.get_post(id)

        form = CreatePost(instance=post)

        return self.render_post(form)

    def post(self, request, id=None):
        post = self.get_post(id)

        username = request.user
        is_user = AuthorUser.objects.filter(author=username, id=id)

        if is_user:
            form = CreatePost(request.POST, request.FILES, instance=post)

            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user

                author_user = AuthorUser.objects.get(author=request.user)

                post.author_cover = author_user

                post.save()

                return redirect('social_echo:home')

        else:
            raise Http404()

        return self.render_post(form)


@method_decorator(
    login_required(login_url='authors:login_author',
                   redirect_field_name='next'
                   ),
    name='dispatch'
)
class PostDeleteView(View):
    def get_post(self, id):
        post = get_object_or_404(Posts, id=id)

        if post.author != self.request.user:
            raise Http404()

        return post

    def post(self, request, id):
        post = self.get_post(id)
        print(post)
        post.delete()

        return redirect('social_echo:home')
