from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Service, Category
from .forms import ProductForm, ServiceForm

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Produit créé avec succès.')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Nouveau Produit'
    })

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit modifié avec succès.')
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': f'Modifier {product.name}'
    })

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Produit supprimé avec succès.')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'products/service_list.html', {'services': services})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Service créé avec succès.')
            return redirect('service_list')
    else:
        form = ServiceForm()
    
    return render(request, 'products/service_form.html', {
        'form': form,
        'title': 'Nouveau Service'
    })


#Service


@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'products/service_list.html', {'services': services})

@login_required
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'products/service_detail.html', {'service': service})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Service créé avec succès.')
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm()
    
    return render(request, 'products/service_form.html', {
        'form': form,
        'title': 'Nouveau Service'
    })

@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service modifié avec succès.')
            return redirect('service_detail', pk=pk)
    else:
        form = ServiceForm(instance=service)
    
    return render(request, 'products/service_form.html', {
        'form': form,
        'title': f'Modifier {service.name}'
    })

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service supprimé avec succès.')
        return redirect('service_list')
    return render(request, 'products/service_confirm_delete.html', {'service': service})