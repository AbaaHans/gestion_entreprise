from django.contrib import admin # type: ignore
from .models import Invoice
# Register your models here.

class FactureAdmin(admin.ModelAdmin):

    list_display = (
        'invoice_number',
        'client',
        'agent',
        'date',
        'due_date',
        'status',
        'notes'
    )

admin.site.register(Invoice,FactureAdmin)
