from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF,shapes




from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import portrait

p = canvas.Canvas("sample25.pdf", pagesize=portrait(letter))

collect = ['Raizen','John','Isaac','Jacob','Newton', 'Gosling', 'Gates']
x = 0

for index in range (len(collect)):
    for j in range(2): 
        qrw = QrCodeWidget(collect[index])
        b = qrw.getBounds()
        w=b[2]-b[0] 
        h=b[3]-b[1] 
        
        d = Drawing(200,100,transform=[300./w,0,0,300./h,0,0]) 
        d.add(shapes.String(45,0,collect[index], textAnchor="middle"))

        d.add(qrw)

        renderPDF.draw(d, p,x,((index%2) *350 ) + 100)
        print(x,((index%2) *350 ) + 100)
        break
    x+=300
    if x ==600:
        x=0
   
    
    if index%4==3:
        p.showPage() 

    
    
p.save()