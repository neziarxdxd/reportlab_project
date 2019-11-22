from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import defaultPageSize
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape



pdfmetrics.registerFont(TTFont('Rale', 'Raleway-Bold.ttf'))
c= canvas.Canvas("sample23.pdf", pagesize=landscape(letter))
c.drawImage("image.png", 350,200, width=350,height=275,mask=None) 
c.setFont('Rale',20)
c.setFillColor(HexColor(0xff8100))
c.drawCentredString(415,500, "Certificate of Completion")
c.setFont('Helvetica',50)
c.setFillColor(HexColor(0xf5d100))
c.drawCentredString(415,400, "RAIZENG SANGALAN RENN")
c.showPage()
c.save()