from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def landing_page(request):
    return render(request, 'firstpage.html')


def second_page(request):
    return HttpResponse("second page")


def count(request):
    angka = 0
    angka = angka+1
    return HttpResponse(str(angka))


def example(request):
    return render(request, 'example.html')


def rama(request):
    return HttpResponse("Hallo brow")


def first_page(request):
    return render(request, 'firstpage.html')
