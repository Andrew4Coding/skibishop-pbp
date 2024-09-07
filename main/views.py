from django.shortcuts import render
from .models import Product

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
        'products': example_products,
    }

    return render(request, 'main.html', context)