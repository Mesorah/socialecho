from django.urls import path
from . import views

app_name = 'social_echo'

urlpatterns = [
     path('', views.home, name="home"),

     path('create_post/', views.create_post, name="create_post"),
     path('edit_post/<int:id>/', views.edit_post, name="edit_post"),
     path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
     path('view_post/<int:id>/', views.view_post, name="view_post"),


     path('dashboard/<int:id>/', views.dashboard, name="dashboard"),
     path('dashboard/follows/<int:id>/', views.list_follows_or_following,
          {'type_': 'follows'}, name="list_follows"),

     path('dashboard/following/<int:id>/', views.list_follows_or_following,
          {'type_': 'following'}, name="list_following"),

     path('dashboard/unfollow_user/<int:id>/', views.unfollow_or_unfollowing,
          {'type_': 'unfollow'}, name="unfollow_user"),

     path('dashboard/unfollowing_user/<int:id>/',
          views.unfollow_or_unfollowing,
          {'type_': 'unfollowing'}, name="unfollowing_user"),

     path('follow/<int:id>/', views.follow_user_system,
          name="follow_user_system"),
     path('unfollow/<int:id>/', views.unfollow_user_system,
          name="unfollow_user_system"),
]
