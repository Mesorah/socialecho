from django import forms
from django.contrib.auth.models import User


class RegisterAuthor(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    cover = forms.ImageField()

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password',]

    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 3:
            self.add_error('username', 'seu username é muito pequeno')

        if User.objects.filter(username=username).exists():
            self.add_error('username', 'esse username já existe')

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            self.add_error('password', 'As senhas não coincidem')

        return password
