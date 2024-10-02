from django import forms
from django.contrib.auth.models import User


class RegisterAuthor(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    cover = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password',
                  'repeat_password',
                  'cover']

    def clean_email(self):
        email = self.cleaned_data['email']

        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            self.add_error('email', 'este e-mail já existe')

        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 3:
            self.add_error('username', 'seu username é muito pequeno')

        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            self.add_error('username', 'esse username já existe')

        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        repeat_password = cleaned_data['repeat_password']

        if password and repeat_password and password != repeat_password:
            self.add_error('password', 'As senhas não coincidem')
            self.add_error('repeat_password', 'As senhas não coincidem')

        if len(password) <= 3:
            self.add_error('password', 'Essa senha é muito curta')

        return cleaned_data


class LoginAuthor(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
