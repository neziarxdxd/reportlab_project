from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF,shapes




from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape

p = canvas.Canvas("sample25.pdf", pagesize=landscape(letter))

collect = ['Raizen','John','Isaac','Jacob','Newton', 'Gosling', 'Gates']
x = 0
y= 0
for data in collect:
    qrw = QrCodeWidget(data) 

    b = qrw.getBounds()

    w=b[2]-b[0] 
    h=b[3]-b[1] 
    
    d = Drawing(200,100,transform=[100./w,0,0,100./h,0,0]) 
    d.add(shapes.String(45,0,data, textAnchor="middle"))

    d.add(qrw)
    
    renderPDF.draw(d, p,10, 10+y)
    y+=100
    x+=30



p.showPage()
p.save()