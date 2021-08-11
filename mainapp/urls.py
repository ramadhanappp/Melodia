from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('man', views.man),
    path('woman', views.woman),
    path('example', views.example),
    path('second', views.second_page),
    path('', views.landing_page),
]
