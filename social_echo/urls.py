from django.urls import path
from . import views

app_name = 'social_echo'

urlpatterns = [
     path('', views.PostListView.as_view(), name="home"),

     path('create_post/',
          views.PostCreateUpdateView.as_view(),
          name="create_post"
          ),
     path('edit_post/<int:id>/',
          views.PostCreateUpdateView.as_view(),
          name="edit_post"
          ),
     path('delete_post/<int:id>/',
          views.PostDeleteView.as_view(),
          name="delete_post"
          ),
     path('view_post/<int:id>/', views.view_post, name="view_post"),
]
