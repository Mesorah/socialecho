from django.shortcuts import render
from .forms import RegisterAuthor


def register_author(request):
    if request.method == 'POST':
        form = RegisterAuthor(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
    else:
        form = RegisterAuthor()

    return render(request, 'authors/pages/register.html', context={
        'form': form
    })
