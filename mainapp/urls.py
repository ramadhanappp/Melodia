from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

    path('secondpage', views.second_page),
    path('firstpage', views.first_page),
    path('rama', views.rama),
    path('example', views.example),
    path('count/<int:angka>/', views.count),
    path('second', views.second_page),
    path('', views.landing_page),
]
