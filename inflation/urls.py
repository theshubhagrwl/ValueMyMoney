from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('graph/', views.graph, name='graph'),
]
