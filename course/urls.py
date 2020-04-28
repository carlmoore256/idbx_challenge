from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='courses-home'), #leave as home page
    path('admin/', views.admin, name='courses-manage')
]
