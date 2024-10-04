from django.urls import path
from . import views

app_name = 'social_echo'

urlpatterns = [
    path('', views.home, name="home"),
    path('create_post/', views.create_post, name="create_post"),
    path('edit_post/<int:id>/', views.edit_post, name="edit_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
    path('view_post/<int:id>/', views.view_post, name="view_post"),
    path('dashboard/', views.dashboard, name="dashboard")
]
