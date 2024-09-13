from django.shortcuts import render, redirect
from .models import Product
from main.forms import ProductEntryForm

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_model(request):
    model = Product.objects.all()

    example_products = [
        {
            "name": "Bintang Skibidi",
            "price": 1000,
            "description": "Skibidi",
        },
        {
            "name": "Doge Coin Plush",
            "price": 25,
            "description": "A plush toy of the Doge meme dog",
        },
        {
            "name": "Keanu Reeves Action Figure",
            "price": 50,
            "description": "A highly detailed action figure of Keanu Reeves",
        },
        {
            "name": "What Do You Meme? Card Game",
            "price": 30,
            "description": "A popular party game based on memes",
        },
        {
            "name": "Fidget Spinner",
            "price": 10,
            "description": "A small, handheld toy that spins rapidly",
        },
        {
            "name": "Among Us Merchandise",
            "price": 15,
            "description": "A variety of products based on the popular online game Among Us",
        },
        {
            "name": "Squid Game Merchandise",
            "price": 20,
            "description": "Items inspired by the hit Netflix series Squid Game",
        },
        {
            "name": "Pet Rock",
            "price": 5,
            "description": "A rock painted to look like a pet",
        },
        {
            "name": "Slap Chop",
            "price": 20,
            "description": "A hand-powered food chopper that became a viral sensation",
        },
        {
            "name": "The Perpetual Motion Machine",
            "price": 100,
            "description": "A device that supposedly operates indefinitely without an external energy source",
        }
    ]
        
    context = {
        'name': 'Andrew Devito Aryo',
        'app_name': 'Skibishop',
        'products': model,
    }

    return render(request, 'main.html', context)

def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main:show_model')
    
    context = {'form': form}
    return render(request, 'Add/create_product.html', context)


def show_all_xml(_):
    data = Product.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_id_xml(_, id: str):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_all_json(_):
    data = Product.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_id_json(_, id: str):
    data = Product.objects.filter(id=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")