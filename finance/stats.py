from datetime import datetime, timedelta
from django.db.models import Sum
from django.utils import timezone
from .models import Invoice

def get_revenue_stats():
    now = timezone.now()
    today = now.date()
    
    # Calculer le début de la semaine (lundi)
    start_of_week = today - timedelta(days=today.weekday())
    # Calculer le début du mois
    start_of_month = today.replace(day=1)
    # Calculer le début de l'année
    start_of_year = today.replace(month=1, day=1)

    return {
        'daily': get_revenue_for_period(today, today),
        'weekly': get_revenue_for_period(start_of_week, today),
        'monthly': get_revenue_for_period(start_of_month, today),
        'yearly': get_revenue_for_period(start_of_year, today)
    }

def get_revenue_for_period(start_date, end_date):
    # Calculer le revenu en FCFA (XAF)
    revenue = Invoice.objects.filter(
        status='paid',
        date__range=[start_date, end_date]
    ).aggregate(
        total=Sum('items__quantity', field='items__quantity * items__unit_price')
    )['total'] or 0
    
    return revenue  # Le montant est déjà en FCFA