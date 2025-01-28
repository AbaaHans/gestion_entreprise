from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from produit.models import Product, Service

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse({
        'id': product.pk,
        'name': product.name,
        'price': str(product.price),
        'stock': product.stock
    })

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return JsonResponse({
        'id': service.pk,
        'name': service.name,
        'price': str(service.price),
        'duration': service.duration
    })