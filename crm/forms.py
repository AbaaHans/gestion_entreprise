from django import forms
from .models import Client, ClientNote

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone','entreprise', 'statut', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'entreprise': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ClientNoteForm(forms.ModelForm):
    class Meta:
        model = ClientNote
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }