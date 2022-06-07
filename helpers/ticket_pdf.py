from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
 


def generate_pdf(turn=None,service=None):
    service_name = service.split(",")[1]
    print(service_name)
    c = canvas.Canvas(f'ticket/{service_name }{str(turn)}.pdf',pagesize=(3*inch ,5*inch))
    # c.line(108, 360, 108,0)
    # c.line(135, 360, 135,0)
    # print(3*inch ,5*inch)
    x = c._pagesize[0] / 2
    try:
        c.setLineWidth(.3)
        fontsize = 20
        c.setFont('Helvetica', 20)
        c.drawCentredString(x,300,'TURNO')
        fontsize = 30
        c.setFont('Helvetica', fontsize)
        c.drawCentredString(x,260,f'{turn}')
        c.setFont('Helvetica', 18)
        fontsize = 18
        # c.drawCentredString(x,230,f'P')

        fontsize = 25
        c.setFont('Helvetica', fontsize)
        
        
        c.drawCentredString(x,205,service_name)
        # print(108-35)
        
    # c.setFont('Helvetica', 20)
    # c.drawString(100,330,f'{service_name }')
    
        c.save()
    except Exception as e:
        print(e)
        return None

    return True


# def position_x(context, fontsize, x_max_size = 216):
#     base_font_size = fontsize / 2
#     pixel_context = len(f'{context}') * base_font_size
#     empty_space = x_max_size - pixel_context
#     return empty_space / 2


# generate_pdf(turn=10,service_name ="Servicio")