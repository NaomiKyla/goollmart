from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from .models import Product
from .forms import ProductForm

# Menampilkan halaman utama dengan daftar semua produk
def show_main(request):
    products = Product.objects.all()
    context = {
        'npm': '2406434102',
        'name': 'Naomi Kyla Zahra Siregar',
        'class': 'PBP B',
        'products': products,
    }
    return render(request, "main.html", context)

# Halaman form untuk membuat produk baru
def create_product(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_main')

    return render(request, "create_product.html", {'form': form})

# Menampilkan halaman detail produk tertentu, sekaligus tambah view count
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    product.views += 1
    product.save()

    return render(request, "product_detail.html", {'product': product})

# Data delivery endpoints 
def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")


def show_xml_by_id(request, product_id):
    item_qs = Product.objects.filter(pk=product_id)
    if not item_qs.exists():
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", item_qs)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json_by_id(request, product_id):
    try:
        item = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    json_data = serializers.serialize("json", [item])
    return HttpResponse(json_data, content_type="application/json")

# test