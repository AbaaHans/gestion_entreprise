from django.contrib import admin

from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'entreprise',
        'statut',
        'address',
    )

admin.site.register(Client,ClientAdmin )