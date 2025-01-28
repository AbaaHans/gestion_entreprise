from reportlab.lib import colors # type: ignore
from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle # type: ignore
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle # type: ignore
from io import BytesIO

def generate_pdf(invoice):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # En-tête
    elements.append(Paragraph(f"Facture #{invoice.invoice_number}", styles['Heading1']))
    elements.append(Spacer(1, 20))

    # Informations client
    elements.append(Paragraph("Informations client:", styles['Heading2']))
    client_info = [
        [Paragraph("Nom:", styles['Normal']), Paragraph(invoice.client.name, styles['Normal'])],
        [Paragraph("Email:", styles['Normal']), Paragraph(invoice.client.email, styles['Normal'])],
        [Paragraph("Téléphone:", styles['Normal']), Paragraph(invoice.client.phone, styles['Normal'])],
        [Paragraph("Adresse:", styles['Normal']), Paragraph(invoice.client.address, styles['Normal'])]
    ]
    client_table = Table(client_info, colWidths=[100, 400])
    client_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(client_table)
    elements.append(Spacer(1, 20))

    # Détails de la facture
    elements.append(Paragraph("Détails de la facture:", styles['Heading2']))
    items_data = [['Description', 'Quantité', 'Prix unitaire', 'Total']]
    for item in invoice.items.all():
        items_data.append([
            item.description,
            str(item.quantity),
            f"{item.unit_price} dhs",
            f"{item.get_total()} dhs"
        ])
    
    # Ajout du total
    items_data.append(['', '', 'Total:', f"{invoice.get_total()} dhs"])
    
    items_table = Table(items_data, colWidths=[250, 75, 100, 75])
    items_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -2), 1, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ]))
    elements.append(items_table)

    # Génération du PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf