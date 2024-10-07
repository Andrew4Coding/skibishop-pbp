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

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='main:login')
def show_main(request):
    cookie = request.COOKIES.get('last_login')

    if cookie:
        last_login = datetime.datetime.strptime(cookie, "%Y-%m-%d %H:%M:%S.%f")
    else:
        return redirect('main:login')
        
    context = {
        'name': 'Andrew Devito Aryo',
        'app_name': 'Skibishop',
        'last_login': last_login
    }

    return render(request, 'index.html', context)

def show_all_xml(request):
    data = Product.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_id_xml(_, id: str):
    data = Product.objects.filter(id=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_all_json(request):
    data = Product.objects.filter(user=request.user)

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
            messages.error(request, "Invalid username or password")
        

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

# CRUD Views
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

@csrf_exempt
@require_POST
def create_product_form_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    user = request.user
    
    new_product = Product(
        name = name,
        price = price,
        description = description,
        user = user
    )
    
    new_product.save()
    
    return HttpResponse(b"CREATED", status=201)
    

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    # Get product entry berdasarkan id
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