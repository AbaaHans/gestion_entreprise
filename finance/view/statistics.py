from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from ..stats import get_revenue_stats
from io import BytesIO

@login_required
def statistics_view(request):
    stats = get_revenue_stats()
    return render(request, 'finance/statistics.html', {
        'stats': stats
    })

@login_required
def print_statistics(request):
    stats = get_revenue_stats()
    
    # Créer le PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Titre
    elements.append(Paragraph("Rapport Financier", styles['Heading1']))
    elements.append(Spacer(1, 20))

    # Tableau des statistiques
    data = [
        ['Période', 'Revenus (FCFA)'],
        ['Aujourd\'hui', f"{stats['daily']:,.0f}"],
        ['Cette semaine', f"{stats['weekly']:,.0f}"],
        ['Ce mois', f"{stats['monthly']:,.0f}"],
        ['Cette année', f"{stats['yearly']:,.0f}"],
    ]

    table = Table(data, colWidths=[200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)

    # Générer le PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()

    # Retourner le PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rapport_financier.pdf"'
    response.write(pdf)
    return response