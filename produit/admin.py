from django.contrib import admin # type: ignore
from .models import Product, Service, Category
# Register your models here.

class ProduitAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'description',
        'price',
        'stock'
    )

   
class ServiceAdmin(admin.ModelAdmin):
     list_display = (
        'name',
        'description',
        'price',
        'duration'
    )

class CategoryAdmin(admin.ModelAdmin):
     list_display = (
          'name',
          'description'
     )



admin.site.register(Product, ProduitAdmin)
admin.site.register(Service)
admin.site.register(Category)

