from datetime import timedelta
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponse
from django import template
import json
from produit.models import Product, Service
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemFormSet
from .utils import generate_pdf

@login_required
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'finance/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'finance/invoice_detail.html', {'invoice': invoice})

@login_required
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            try:
                # Sauvegarde de la facture
                invoice = form.save(commit=False)
                invoice.agent = request.user
                invoice.date = invoice.date or timezone.now().date()
                invoice.due_date = invoice.due_date or (invoice.date + timedelta(days=30))
                invoice.save()
                
                # Sauvegarde des éléments de la facture
                formset.instance = invoice
                items = formset.save(commit=False)
                for item in items:
                    # Si un produit est sélectionné, utiliser ses informations
                    if item.product:
                        if not item.description:
                            item.description = item.product.name
                        if not item.unit_price:
                            item.unit_price = item.product.price
                    # Si un service est sélectionné, utiliser ses informations
                    elif item.service:
                        if not item.description:
                            item.description = item.service.name
                        if not item.unit_price:
                            item.unit_price = item.service.price
                    item.save()
                
                # Supprimer les éléments marqués pour suppression
                for obj in formset.deleted_objects:
                    obj.delete()
                
                messages.success(request, 'Facture créée avec succès.')
                return redirect('invoice_list')
            except Exception as e:
                messages.error(request, f'Erreur lors de la création de la facture: {str(e)}')
        else:
            if form.errors:
                messages.error(request, 'Erreurs dans le formulaire principal')
            if formset.errors:
                messages.error(request, 'Erreurs dans les articles de la facture')
    else:
        initial = {
            'date': timezone.now().date(),
            'due_date': timezone.now().date() + timedelta(days=30)
        }
        form = InvoiceForm(initial=initial)
        formset = InvoiceItemFormSet()
    
    return render(request, 'finance/invoice_form.html', {
        'form': form,
        'formset': formset,
        'title': 'Nouvelle Facture'
    })

@login_required
def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = InvoiceItemFormSet(request.POST, instance=invoice)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Facture modifiée avec succès.')
            return redirect('invoice_detail', pk=pk)
    else:
        form = InvoiceForm(instance=invoice)
        formset = InvoiceItemFormSet(instance=invoice)
    
    return render(request, 'finance/invoice_form.html', {
        'form': form,
        'formset': formset,
        'title': f'Modifier Facture #{invoice.invoice_number}'
    })

@login_required
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        messages.success(request, 'Facture supprimée avec succès.')
        return redirect('invoice_list')
    return render(request, 'finance/invoice_confirm_delete.html', {'invoice': invoice})


@require_POST
def update_invoice_status(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    new_status = request.POST.get('status')
    if new_status in dict(Invoice.STATUS_CHOICES):
        invoice.status = new_status
        invoice.save()
        return JsonResponse({
            'status': 'success',
            'new_status': invoice.get_status_display()
        })
    return JsonResponse({'status': 'error'}, status=400)
# @require_POST
# def update_invoice_status(request, pk):
#     invoice = get_object_or_404(Invoice, pk=pk)
#     new_status = request.POST.get('status')
#     if new_status in dict(Invoice.STATUS_CHOICES):
#         invoice.status = new_status
#         invoice.save()
#         return JsonResponse({
#             'status': 'success',
#             'new_status': invoice.get_status_display()
#         })
#     return JsonResponse({'status': 'error'}, status=400)

def get_product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return JsonResponse({
        'price': str(product.price),
        'name': product.name
    })

def get_service_details(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return JsonResponse({
        'price': str(service.price),
        'name': service.name
    })

@login_required
def invoice_print(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    pdf = generate_pdf(invoice)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="facture_{invoice.invoice_number}.pdf"'
    return response



