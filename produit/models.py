from django.db import models # type: ignore

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catégorie")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    duration = models.IntegerField(verbose_name="Durée (minutes)")
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Service"
        verbose_name_plural = "Services"

