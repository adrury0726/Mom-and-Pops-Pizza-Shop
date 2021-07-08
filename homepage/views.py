# pages/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.models import Product
#from .homepage import Homepage

def index(request):
    #return HttpResponse("<h1>Mom and Pops Pizza Shop</h1>")

    # Render the HTML template index.html with the data in the context variable
    #return render(request, 'homeapge/homepage.html', {)
    return render(request, 'homepage/homepage.html', {})
