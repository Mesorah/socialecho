from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.AuthorRegister.as_view(), name="register_author"),
    path('login/', views.AuthorLogin.as_view(), name="login_author"),
    path('logout/', views.AuthorLogout.as_view(), name="logout_author")
]
