from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Supplier
from .forms import SupplierForm

@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/list.html', {'suppliers': suppliers})

@login_required
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'suppliers/detail.html', {'supplier': supplier})

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save()
            messages.success(request, 'Fournisseur créé avec succès.')
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    
    return render(request, 'suppliers/form.html', {
        'form': form,
        'title': 'Nouveau Fournisseur'
    })

@login_required
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fournisseur modifié avec succès.')
            return redirect('supplier_detail', pk=pk)
    else:
        form = SupplierForm(instance=supplier)
    
    return render(request, 'suppliers/form.html', {
        'form': form,
        'title': f'Modifier {supplier.name}'
    })

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'Fournisseur supprimé avec succès.')
        return redirect('supplier_list')
    return render(request, 'suppliers/delete.html', {'supplier': supplier})