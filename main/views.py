from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()
    return render(request, "main.html", {"products": products})
