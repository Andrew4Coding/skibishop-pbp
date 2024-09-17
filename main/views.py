from django.shortcuts import render, redirect
from .models import Product
from main.forms import ProductEntryForm

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_model(request):
    model = Product.objects.all()

    context = {
        'name': 'Andrew Devito Aryo',
        'app_name': 'Skibishop',
        'products': model,
    }

    return render(request, 'index.html', context)

def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main:show_model')
    
    context = {'form': form}
    return render(request, 'add/create_product.html', context)

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