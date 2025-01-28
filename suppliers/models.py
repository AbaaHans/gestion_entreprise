from django.db import models

class BusinessSector(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Secteur d'activité"
        verbose_name_plural = "Secteurs d'activité"

class SupplierType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type de fournisseur"
        verbose_name_plural = "Types de fournisseur"

class Supplier(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Code fournisseur")
    name = models.CharField(max_length=200, verbose_name="Nom")
    supplier_type = models.ForeignKey(SupplierType, on_delete=models.SET_NULL, null=True, verbose_name="Type de fournisseur")
    business_sector = models.ForeignKey(BusinessSector, on_delete=models.SET_NULL, null=True, verbose_name="Secteur d'activité")
    address = models.TextField(verbose_name="Adresse complète")
    phone = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    email = models.EmailField(verbose_name="Email")
    product_types = models.TextField(verbose_name="Types de produits/services")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"
        ordering = ['name']
