from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
]
