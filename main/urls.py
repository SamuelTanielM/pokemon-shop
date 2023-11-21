from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('json_user/', show_json_by_user, name='show_json_by_user'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    
    path('delete', delete, name="delete"),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase_item/<int:id>/', increase_item_amount, name='increase_item_amount'),
    path('decrease_item/<int:id>/', decrease_item_amount, name='decrease_item_amount'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete_product_ajax/<int:item_id>/', delete_product_ajax, name='delete_product_ajax'),    
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    
]
