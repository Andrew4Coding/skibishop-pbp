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
@login_required(login_url='main:login')
def show_main(request):
    model = Product.objects.filter(user=request.user)

    context = {
        'name': 'Andrew Devito Aryo',
        'app_name': 'Skibishop',
        'products': model,
        'last_login': request.COOKIES.get('last_login')
    }

    return render(request, 'index.html', context)


@login_required(login_url="main:login")
def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form, 
                'last_login': request.COOKIES.get('last_login')
               }
    return render(request, 'crud/create_product.html', context)

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
   if (request.user.is_authenticated):
        return redirect('main:show_main')
   
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
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

def show_profile(request):
    return render(request, 'profile.html')

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form, 
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "crud/edit_product.html", context)