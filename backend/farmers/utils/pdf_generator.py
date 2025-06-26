from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
import tempfile

def generate_distribution_pdf(distribution):
    # Create a temporary PDF file
    result = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    c = canvas.Canvas(result.name, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Seed Track")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 70, "Seed Distribution Receipt")

    # Distribution Info
    c.setFont("Helvetica", 10)
    top = height - 100
    c.drawString(40, top, f"Farmer: {distribution.farmer.full_name}")
    c.drawString(40, top - 15, f"Agent: {distribution.agent.username}")
    c.drawString(40, top - 30, f"Date: {distribution.distributed_at.strftime('%Y-%m-%d')}")

    # Table Data
    data = [["Species", "Quantity"]]
    for item in distribution.items.all():
        data.append([item.species.name, str(item.quantity)])

    table = Table(data, colWidths=[250, 100])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ]))

    # Position table
    table.wrapOn(c, width, height)
    table.drawOn(c, 40, top - 150)

    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width / 2, 30, "© 2025 bn_e. All rights reserved.")

    c.showPage()
    c.save()
    result.seek(0)
    return result
