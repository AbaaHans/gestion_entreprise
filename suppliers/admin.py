from django.contrib import admin

from .models import Supplier, BusinessSector, SupplierType

class FournisseurAdmin(admin.ModelAdmin):
     list_display = {
          'code',
          'name',
          'supplier_type',
          'business_sector',
          'adress',
          'phone',
          'email',
          'product_types'

     }

class SecteurActivitéAdmin(admin.ModelAdmin):
     list_display = {
          'name',
          'description'
     }

class TypeFournisseurAdmin(admin.ModelAdmin):
     list_display = {
           'name',
          'description'
     }

admin.site.register(Supplier)
admin.site.register(BusinessSector)
admin.site.register(SupplierType)

