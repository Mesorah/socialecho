from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_author, name="register_author"),
    path('login/', views.login_author, name="login_author"),
    path('logout/', views.logout_author, name="logout_author")
]
