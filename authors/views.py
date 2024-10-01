from django.shortcuts import render, redirect
from .forms import RegisterAuthor, LoginAuthor
from authors.models import AuthorUser
from django.contrib.auth import authenticate, login, logout


def register_author(request):
    cover = None

    if request.method == 'POST':
        form = RegisterAuthor(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            cover = form.cleaned_data['cover']

            if cover is None:
                cover = 'media/user/base/base_cover.jpeg'

            # cover = form.cleaned_data.get('cover',
            #                               'media/user/base/base_cover.jpeg')

            AuthorUser.objects.create(
                author=user,
                cover=cover
            )

            return redirect('social_echo:home')

    else:
        form = RegisterAuthor()

    return render(request, 'global/pages/base_form.html', context={
        'form': form,
        'cover': cover
    })


def login_author(request):
    if request.method == 'POST':
        form = LoginAuthor(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('social_echo:home')

    else:
        form = LoginAuthor()

    return render(request, 'global/pages/base_form.html', context={
        'form': form,
    })


def logout_author(request):
    logout(request)

    return redirect('social_echo:home')
