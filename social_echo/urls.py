from django.urls import path
from . import views

app_name = 'social_echo'

urlpatterns = [
    path('', views.home, name="home")
]
