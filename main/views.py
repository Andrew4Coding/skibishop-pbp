import datetime
from django.shortcuts import render, redirect
from .models import Product
from main.forms import ProductEntryForm

from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 
from django.contrib import messages

from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.
def show_model(request):
    model = Product.objects.all()

    context = {
        'name': 'Andrew Devito Aryo',
        'app_name': 'Skibishop',
        'products': model,
    }

    return render(request, 'index.html', context)


@login_required(login_url="main:login_user")
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


# Authentication Views
def register(request):
    form = UserCreationForm()

    if (request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been created")
            return redirect('main:login')
        
    context = {'form': form }
    return render(request, 'auth/register.html', context)


def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_model'))
            response.set_cookie('last_login', datetime.datetime.now())
            return response

   else:
      form = AuthenticationForm(request)

   context = {'form': form}
   return render(request, 'auth/login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response