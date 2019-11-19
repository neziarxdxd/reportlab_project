from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape

c= canvas.Canvas("sample22.pdf", pagesize=landscape(letter))
c.setFont('Helvetica',30)
c.drawCentredString(415,500, "Certificate of Completion")
c.showPage()
c.save()