from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    return render(request, 'main.html')

def show_model(request):
    model = Product.objects.all()
    context = {
        'name': 'Andrew Devito Aryo',
        'app_name': 'Skibishop',
        'products': model
    }
    return render(request, 'model.html', context)