from django.urls import path

from . import views

urlpatterns = [
    path('search', views.search_guest, name='search_guest'),
    path('detail/<userid>', views.guest_detail, name='guest_detail'),
]