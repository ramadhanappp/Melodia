from mainapp.models import category, product
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
    try:
        category_yamaha = category.objects.get(pk=1)
        product_yamaha = product.objects.filter(category=category_yamaha)
        return render(request, "yamaha.html", {'product_list': product_yamaha})

    except:
        return HttpResponse("error")


def lakewood(request):
    return render(request, "lakewood.html")


def akustik_yamaha(request):
    return render(request, "akustik_yamaha.html")


def akustik_yamaha_list(request):
    return render(request, 'akustik_yamaha_list.html')
