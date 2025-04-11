from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

post_api_route = SimpleRouter()
post_api_route.register(
    'api',
    views.PostAPIModelViewSet,
    basename='post_api'
)

app_name = 'social_echo'

urlpatterns = [
     path('', views.PostListViewHome.as_view(), name="home"),

     path('create_post/',
          views.PostCreateView.as_view(),
          name="create_post"
          ),
     path('edit_post/<int:pk>/',
          views.PostUpdateView.as_view(),
          name="edit_post"
          ),
     path('delete_post/<int:pk>/',
          views.PostDeleteView.as_view(),
          name="delete_post"
          ),
     path('view_post/<int:pk>/',
          views.ViewPostDetailView.as_view(),
          name="view_post"
          ),
]

urlpatterns += post_api_route.urls
