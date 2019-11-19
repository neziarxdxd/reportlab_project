from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF,shapes
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import portrait

p = canvas.Canvas("readyforpint.pdf", pagesize=portrait(letter))
collect = ['Raizen0','a','c','A','dsdsf','fdfdfdfd']
a = 0
for x in range (len(collect)):
    qrw = QrCodeWidget(collect[x])
    b = qrw.getBounds()
    w=b[2]-b[0] 
    h=b[3]-b[1] 
    d = Drawing(200,50,transform=[280./w,0,0,280./h,0,0]) 
    d.add(shapes.String(45,0,collect[x], textAnchor="middle",fontName="Helvetica",fontSize=12))
    d.add(shapes.String(45,-6,"For testing names", textAnchor="middle",fontName="Helvetica",fontSize=6))
    d.add(qrw)

    renderPDF.draw(d, p, (a%2)*300, ((x%2)*350)+100 )
    print( (a%2)*300, ((x%2)*350)+100)
    if x%2==0:
        a+=1
    if x%4==3:
        p.showPage()  
p.save()