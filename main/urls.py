from django.urls import path
from main.views import show_model, create_product_form

app_name = 'main'

urlpatterns = [
    path('', show_model, name='show_model'),
    path('add/', create_product_form, name='create_product_form'),
]