from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

urlpatterns = [
  path('login', views.LoginView.as_view()),
  url(r'^api-jwt-auth/$', obtain_jwt_token),
  url(r'^api-jwt-auth/refresh/$', refresh_jwt_token),
  url(r'^api-jwt-auth/verify/$', verify_jwt_token),
]