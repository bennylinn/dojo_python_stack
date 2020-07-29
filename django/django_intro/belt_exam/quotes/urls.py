from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('quotes', views.quotes),
    path('login', views.login),
    path('logout', views.logout),
    path('create', views.create),
    path('delete', views.delete),
    path('like', views.like),
    path('user/<int:id>', views.user),
    path('myaccount/<int:id>', views.myaccount),
    path('update/<int:id>', views.update)
]