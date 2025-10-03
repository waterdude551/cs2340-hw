from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='petitions.index'),
    path('create/', views.create_petition_screen, name='petitions.create_petition_screen'),
    path('create/submit/', views.create_petition, name='petitions.create_petition'),
    path('vote/<int:id>/', views.vote, name='petitions.vote'),
    path('unvote/<int:id>/', views.unvote, name='petitions.unvote'),
]