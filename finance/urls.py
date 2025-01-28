from django.urls import path
from finance import views as finance_views
from .view import statistics_view, print_statistics

urlpatterns = [
     # Finance
    path('invoices/', finance_views.invoice_list, name='invoice_list'),
    path('invoices/create/', finance_views.invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/', finance_views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:pk>/update/', finance_views.invoice_update, name='invoice_update'),
    path('invoices/<int:pk>/delete/', finance_views.invoice_delete, name='invoice_delete'),
    path('invoices/<int:pk>/print/', finance_views.invoice_print, name='invoice_print'),
    path('invoices/<int:pk>/update-status/', finance_views.update_invoice_status, name='update_invoice_status'),

    # Statistiques
    path('statistics/', statistics_view, name='finance_statistics'),
    path('statistics/print/', print_statistics, name='print_statistics'),
]