from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('profile/<int:id>/', views.home, name="home"),
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
