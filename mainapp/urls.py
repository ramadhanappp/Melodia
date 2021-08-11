from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

    path('firstpage', views.first_page),
    path('rama', views.rama),
    path('example', views.example),
    path('count/<int:angka>/', views.count),
    path('second', views.second_page),
    path('', views.first_page),
]
