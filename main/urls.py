from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_product, delete_product
from main.views import add_product_entry_ajax, ajax_login, ajax_register
from main.views import ajax_add_product, ajax_get_product, ajax_edit_product, ajax_delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product, name='create_product'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-product-entry-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path("ajax-login/", ajax_login, name="ajax_login"),
    path("ajax-register/", ajax_register, name="ajax_register"),
    path("ajax/add-product/", ajax_add_product, name="ajax_add_product"),
    path("ajax/get-products/", ajax_get_product, name="ajax_get_product"),
    path("ajax/edit-product/<uuid:id>/", ajax_edit_product, name="ajax_edit_product"),
    path("ajax/delete-product/<uuid:id>/", ajax_delete_product, name="ajax_delete_product"),
]