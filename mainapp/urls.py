from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('example', views.example),
    path('count/<int:angka>/', views.count),
    path('second', views.second_page),
    path('', views.landing_page),
]
