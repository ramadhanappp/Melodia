from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('akustik_yamaha', views.akustik_yamaha),
    path('lakewood', views.lakewood),
    path('yamaha', views.yamaha),
    path('cort', views.cort),
    path('example', views.example),
    path('second', views.second_page),
    path('', views.landing_page),
]
