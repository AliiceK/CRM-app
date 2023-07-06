from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('product/', views.product),
    path('customer/', views.customer),


]