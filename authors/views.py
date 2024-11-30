from .forms import RegisterAuthor
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class AuthorRegister(FormView):
    template_name = 'global/pages/base_form.html'
    form_class = RegisterAuthor
    success_url = reverse_lazy('social_echo:home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Register',
        })

        return context

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)


class AuthorLogin(LoginView):
    template_name = 'global/pages/base_form.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('social_echo:home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Login',
        })

        return context

    def get_success_url(self):
        return self.success_url


@method_decorator(
    login_required(login_url='authors:login_author',
                   redirect_field_name='next'
                   ),
    name='dispatch'
)
class AuthorLogout(LogoutView):
    def get_redirect_url(self):
        return reverse_lazy('authors:login_author')
