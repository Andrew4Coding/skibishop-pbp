from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', create_product_form, name='create_product_form'),
    path('xml/', show_all_xml, name='show_all_xml'),
    path('xml/<str:id>/', show_id_xml, name='show_id_xml'),
    path('json/', show_all_json, name='show_all_json'),
    path('json/<str:id>/', show_id_json, name='show_id_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', show_profile, name='profile'),
    path('delete/<uuid:id>', delete_product, name='delete'),
    path('edit/<uuid:id>', edit_product, name='edit'),
]