from django.urls import path
from . import views

app_name = 'social_echo'

urlpatterns = [
    path('', views.home, name="home"),
    path('create_post/', views.create_post, name="create"),
]
