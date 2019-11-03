from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape

p = canvas.Canvas("sample22.pdf", pagesize=landscape(letter))
data = 'Helo World!'
qrw = QrCodeWidget(data) 

b = qrw.getBounds()

w=b[2]-b[0] 
h=b[3]-b[1] 
p.drawString(160,20,data)
d = Drawing(200,100,transform=[330./w,0,0,330./h,0,0]) 
d.add(qrw)

renderPDF.draw(d, p, 10, 10)


p.showPage()
p.save()