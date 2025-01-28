from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from crm.models import Client
from produit.models import Product, Service
from suppliers.models import Supplier
from finance.models import Invoice

@login_required
def dashboard(request):
    context = {
        'clients_count': Client.objects.count(),
        'products_count': Product.objects.count(),
        'suppliers_count': Supplier.objects.count(),
        'services_count': Service.objects.count(),
        'invoices_count': Invoice.objects.count(),
        'recent_clients': Client.objects.all()[:3],
        'recent_invoices': Invoice.objects.all()[:3],
        'low_stock_products': Product.objects.filter(stock__lte=10),
    }
    return render(request, 'dashboard.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')