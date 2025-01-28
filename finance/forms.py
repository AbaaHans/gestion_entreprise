from django import forms 
from django.forms import ValidationError, inlineformset_factory 
from .models import Invoice, InvoiceItem
from produit.models import Product, Service



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'client','status', 'date', 'due_date', 'notes']
        widgets = {
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),  
            'client': forms.Select(attrs={'class': 'form-select'}),
            'status' : forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  
        }
class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'service', 'description', 'quantity', 'unit_price']

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        service = cleaned_data.get('service')
        description = cleaned_data.get('description')
        quantity = cleaned_data.get('quantity')
        unit_price = cleaned_data.get('unit_price')

        # Vérifier qu'au moins un produit ou service est sélectionné
        if not product and not service:
            raise ValidationError("Vous devez sélectionner soit un produit soit un service.")

        # Empêcher la sélection simultanée d'un produit et d'un service
        if product and service:
            raise ValidationError("Vous ne pouvez pas sélectionner à la fois un produit et un service.")

        # Vérifier les champs obligatoires
        if not description:
            self.add_error('description', 'Ce champ est obligatoire.')
        if not quantity:
            self.add_error('quantity', 'Ce champ est obligatoire.')
        if not unit_price:
            self.add_error('unit_price', 'Ce champ est obligatoire.')

        return cleaned_data
   
   
    notes = forms.CharField(label='Notes', widget=forms.Textarea(attrs={'rows': 3}))
    produit = forms.ModelChoiceField(label='Produit', queryset=Product.objects.all())
    service = forms.ModelChoiceField(label='Service', queryset=Service.objects.all())
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows': 3}))
    quantité = forms.IntegerField(label='Quantité')
    unit_prix = forms.DecimalField(label='Prix Unitaire')


InvoiceItemFormSet = inlineformset_factory(
    Invoice,
    InvoiceItem,
    fields=['product', 'service', 'description', 'quantity', 'unit_price'],
    widgets={
        'product': forms.Select(attrs={'class': 'form-select'}),  
        'service': forms.Select(attrs={'class': 'form-select'}),  
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 
        'quantity': forms.NumberInput(attrs={'class': 'form-control'}),  
        'unit_price': forms.NumberInput(attrs={'class': 'form-control'})
        
    },
    extra=1,
    can_delete=True

    
)