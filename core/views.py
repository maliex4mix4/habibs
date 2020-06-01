from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

class HomeView(ListView):
    model = Item
    template_name = "home-page.html"     

def checkout_page(request):

    return render(request, "checkout-page.html")

def products(request):
    
    products = Item.objects.all()

    print(products)

    return render(request, 'products.html', {'products': products,}) 

class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"    