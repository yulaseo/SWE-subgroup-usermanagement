from django.urls import path

from . import views

urlpatterns = [
    path('list', views.feedback_list, name='feedback_list'),
    path('detail/<id>', views.feedback_detail, name='feedback_detail'),
]