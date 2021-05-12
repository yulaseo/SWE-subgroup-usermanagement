from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delres', views.delete_or_restrict, name='delete_restrict'),
]