from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Client(models.Model):

    STATUT_CHOICES = [
        ('prospect', 'Prospect'),
        ('client_actif', 'Client Actif'),
        ('client_inactif', 'Client Inactif'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Téléphone") 
    address = models.TextField(verbose_name="Adresse")
    entreprise = models.CharField(max_length=200, blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='prospect')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class ClientNote(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='notes')
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Note client"
        verbose_name_plural = "Notes clients"