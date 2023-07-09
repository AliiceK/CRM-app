from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.


def Home(request):
    return render(request, 'accounts/dashboard.html')


def product(request):
    product = Product.objects.all()
    return render(request, 'accounts/product.html', {'products' : product})

def customer(request):
    return render(request, 'accounts/customer.html')
