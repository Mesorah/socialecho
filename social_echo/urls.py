from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

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

     path(
         'api/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'
     ),
     path(
         'api/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
     ),
     path(
         'api/token/verify/',
         TokenVerifyView.as_view(),
         name='token_verify'
     ),
]

urlpatterns += post_api_route.urls
