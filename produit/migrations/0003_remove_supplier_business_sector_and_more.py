# Generated by Django 5.1.4 on 2024-12-21 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_businesssector_suppliertype_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='business_sector',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='supplier_type',
        ),
        migrations.DeleteModel(
            name='BusinessSector',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='SupplierType',
        ),
    ]
