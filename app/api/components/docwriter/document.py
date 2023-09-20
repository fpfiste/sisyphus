import os
from reportlab.lib import pagesizes
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas





class Document():
    def __init__(self,doc_id, doc_type, language:str='de', output_path:str = '.'):
        self.document_id = doc_id
        self.document_type = doc_type
        self.language = language
        self.output_path = output_path
        self.logo = None
        self.customer = None
        self.company = None
        self.positions = []
        self.file_name = os.path.join(self.output_path, f'{self.document_type}-{self.document_id}.pdf')
        self.page_counter = 0


    def set_logo(self, logo_path:str='',  logo_width=550, logo_height=120, logo_x=0, logo_y=0):

        if os.path.exists(logo_path):
            self.logo = {
                'logo_path' : logo_path,
                'logo_width' : logo_width,
                'logo_height': logo_height,
                'logo_x' : logo_x,
                'logo_y' : logo_y
            }
        else:
            print(logo_path)
            raise Exception('logo path not found')
    def set_customer(self,  id, name, address, pcode, city, country):
        self.customer = {
            'id' : id,
            'name': name,
            'address' : address,
            'pcode' : pcode,
            'city' : city,
            'country' : country
        }

    def set_company(self, name, address, pcode, city, country, agent, email, phone, vat_number):
        self.company = {
            'name': name,
            'address' : address,
            'pcode' : pcode,
            'city' : city,
            'country' : country,
            'agent' : agent,
            'email' : email,
            'phone' : phone,
            'vat_number' : vat_number
        }

    def draw_template(self):

        assert self.logo != None, 'Logo is missing'
        assert self.customer != None, 'Customer is missing'
        assert self.company != None ,'company is missing'

        file_name = os.path.join(self.file_name)
        c = canvas.Canvas(file_name, pagesize=pagesizes.A4, bottomup=0)

        #c.translate(10, 100)

        ## Logo
        c.scale(1, -1)
        c.setLineWidth(0.2)
        x_margin = self.logo['logo_x'] * mm
        y_margin = self.logo['logo_y'] * mm
        w = self.logo['logo_width'] * mm
        h = self.logo['logo_height'] *mm
        c.drawImage(self.logo['logo_path'], x_margin, -( y_margin+h), width=w, height=h)
        # Title Section
        # Again Inverting Scale For strings insertion
        c.scale(1, -1)
        # Again Setting the origin back to (0,0) of top-left
        #·c.translate(-10, -40)




        c.setFont("Helvetica", 6)

        c.drawString(13 * cm, 6 * cm, f'{self.company["name"]}, {self.company["address"]}, {self.company["pcode"]}-{self.company["city"]}')
        c.setFont("Helvetica", 11)
        c.drawString(13 * cm, 6.5 * cm, self.customer['name'])
        c.drawString(13 * cm, 7 * cm, self.customer['address'])
        c.drawString(13 * cm, 7.5 * cm, f'{self.customer["pcode"]} {self.customer["city"]}')

        c.setFont("Helvetica", 8)
        c.drawString(2 * cm, 6 * cm,  self.company['name'])
        c.drawString(2 * cm, 6.5 * cm, self.company['address'])
        c.drawString(2 * cm, 7 * cm, f'{self.company["country"]}-{self.company["pcode"]} {self.company["city"]}')
        c.drawString(2 * cm, 7.5 * cm, f"MWST-NR: { self.company['vat_number']}")

        return c

    def addy(self, ypos, canvas, amount):
        ypos += amount
        if ypos >=26:
            self.page_counter += 1
            page_num = canvas.getPageNumber()
            canvas.drawString(18 * cm, 29* cm, 'Seite: ' + str(page_num))
            canvas.showPage()
            ypos = 3
            canvas.setFont("Helvetica", 10)
        return ypos
