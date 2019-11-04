from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF,shapes

from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import portrait

p = canvas.Canvas("sizestest.pdf", pagesize=portrait(letter))

collect = ['Raizen','John','Isaac','Jacob','Newton', 'Gosling', 'Gates']
qrw = QrCodeWidget(collect[0])
b = qrw.getBounds()
w=b[2]-b[0] 
h=b[3]-b[1] 
d = Drawing(200,100,transform=[300./w,0,0,300./h,0,0]) 
d.add(shapes.String(45,0,collect[0], textAnchor="middle"))
d.add(qrw)
renderPDF.draw(d, p,0,100)



qrw = QrCodeWidget(collect[1])
b = qrw.getBounds()
w=b[2]-b[0] 
h=b[3]-b[1] 
d = Drawing(200,100,transform=[300./w,0,0,300./h,0,0]) 
d.add(shapes.String(45,0,collect[1], textAnchor="middle"))
d.add(qrw)
renderPDF.draw(d, p,300,100)


qrw = QrCodeWidget(collect[2])
b = qrw.getBounds()
w=b[2]-b[0] 
h=b[3]-b[1] 
d = Drawing(200,100,transform=[300./w,0,0,300./h,0,0]) 
d.add(shapes.String(45,0,collect[1], textAnchor="middle"))
d.add(qrw)
renderPDF.draw(d, p,300,450)
p.save()