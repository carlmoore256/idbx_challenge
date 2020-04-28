from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='courses-home'), #leave as home page
    path('about/', views.about, name='courses-about'),
]
