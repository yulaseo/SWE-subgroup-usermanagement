from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('give', views.give_feedback, name='give_feedback'),
    path('reply', views.reply_feedback, name='reply_feedback'),
]