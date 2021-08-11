from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def landing_page(request):
    return render(request, "firstpage.html")


def second_page(request):
    return render(request, "secondpage.html")


def example(request):
    return render(request, 'example.html')


def cort(request):
    return render(request, 'cort.html')


def yamaha(request):
    return render(request, "yamaha.html")

def lakewood(request):
    return render(request, "lakewood.html")
