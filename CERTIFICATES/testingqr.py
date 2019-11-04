from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF,shapes
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import portrait

p = canvas.Canvas("sample39.pdf", pagesize=portrait(letter))
collect = ['Raizen','Galileo','Isaac','Thank you LORD','Newton', 'Gosling', 'Gates']
a = 0
for x in range (len(collect)):
    qrw = QrCodeWidget(collect[x])
    b = qrw.getBounds()
    w=b[2]-b[0] 
    h=b[3]-b[1] 
    d = Drawing(200,100,transform=[300./w,0,0,300./h,0,0]) 
    d.add(shapes.String(45,0,collect[x], textAnchor="middle",fontName="Helvetica"))
    d.add(qrw)

    renderPDF.draw(d, p, (a%2)*300, ((x%2)*350)+100 )
    print( (a%2)*300, ((x%2)*350)+100)
    if x%2==0:
        a+=1
    if x%4==3:
        p.showPage()  
p.save()