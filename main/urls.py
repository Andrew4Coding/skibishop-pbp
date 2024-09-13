from django.urls import path
from main.views import show_model, create_product_form, show_all_json, show_all_xml, show_id_json, show_id_xml

app_name = 'main'

urlpatterns = [
    path('', show_model, name='show_model'),
    path('add/', create_product_form, name='create_product_form'),
    path('xml/', show_all_xml, name='show_all_xml'),
    path('xml/<str:id>/', show_id_xml, name='show_id_xml'),
    path('json/', show_all_json, name='show_all_json'),
    path('json/<str:id>/', show_id_json, name='show_id_json'),
]