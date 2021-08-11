from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('secondpage/', views.secondpage),
    path('firstpage/', views.firstpage),
    path('rama', views.rama),
    path('example/', views.example),
    path('count/<int:angka>/', views.count),
    path('second', views.secondpage),
    path('', views.landing_page),
]
