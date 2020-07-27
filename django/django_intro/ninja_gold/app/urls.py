from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('farm', views.farm),
    path('cave', views.cave),
    path('house', views.house),
    path('casino', views.casino)
]