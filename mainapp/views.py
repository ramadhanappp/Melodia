from mainapp.models import brand, category, product
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
        print(request.GET)
        brand_gitar = brand.objects.get(pk=2)
        product_gitar = product.objects.filter(merk=brand_gitar)
        if (product_gitar.count() != 0):
            return render(request, "yamaha.html", {"product_list": product_gitar, "available": True})
        else:
            return render(request, "yamaha.html", {"available": False})
    except:
        return HttpResponse("ERROR")


def lakewood(request):
    return render(request, "lakewood.html")


def akustik_yamaha(request):
    return render(request, "akustik_yamaha.html")


def akustik_yamaha_list(request):
    return render(request, 'akustik_yamaha_list.html')
