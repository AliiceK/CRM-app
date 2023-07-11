from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('product/', views.product),
    path('customer/<str:pk_test>/', views.customer),


]