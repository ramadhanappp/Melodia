from mainapp.models import brand
from mainapp.models import product
from mainapp.models import category
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views, api
from django.core import serializers
import json


urlpatterns = [

    path('yamaha/akustik', views.akustik_yamaha),
    path('yamaha/akustik/list', views.akustik_yamaha_list),
    path('lakewood', views.lakewood),
    path('yamaha', views.yamaha),
    path('cort', views.cort),
    path('example', views.example),
    path('second', views.second_page),
    path("api/category/get-all/", api.get_categories),
    path("api/category/create/", api.create_categories),
    path("api/product/get-all/", api.get_products),
    path("api/brand/get-all/", api.get_brands),
    path('', views.landing_page),

]
