import io
import os
from reportlab.lib import pagesizes, colors
from reportlab.lib.units import cm, mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas





class Document():
    def __init__(self,doc_id, doc_type, language:str='de', output_path:str = '.'):
        self.document_id = doc_id
        self.document_type = doc_type
        self.language = language
        self.logo = None
        self.output_path = output_path
        self.customer = None
        self.company = None
        self.positions = []
        self.file_name = os.path.join(output_path, f'{self.document_type}-{self.document_id}.pdf')
        self.c = canvas.Canvas(self.file_name, pagesize=self.page_size, bottomup=0)
        self.page_width , self.page_height = self.c._pagesize
        self.y = 4
        self.x = 4
        self.footer_size = 3
        self.max_pages = 1
        self.settings = {
            'font' : 'Helvetica',
            'font-size': 10,
            'stroke-color':colors.black,
            'line-width' : 0.25,
            'fill-color': colors.black
        }



    def setFont(self, font:str, size:int):
        self.settings['font'] = font
        self.settings['font-size'] = size
        self.apply_settings()

    def setStrokeColor(self, color):
        self.settings['stroke-color'] = color
        self.apply_settings()

    def setLineWidth(self, width:float):
        self.settings['line-width'] = width
        self.apply_settings()


    def setFillColor(self, color):
        self.settings['fill-color'] = color
        self.apply_settings()


    def apply_settings(self):
        self.c.setFont(self.settings['font'], self.settings['font-size'])
        self.c.setStrokeColor(self.settings['stroke-color'])
        self.c.setLineWidth(self.settings['line-width'])
        self.c.setFillColor(self.settings['fill-color'])


    def set_logo(self, logo:str='',  logo_width=550, logo_height=120, logo_x=0, logo_y=0):
        self.logo = {
            'logo' : logo,
            'logo_width' : float(logo_width) if logo_width != ' ' else 0,
            'logo_height': float(logo_height)  if logo_height != ' ' else 0,
            'logo_x' : float(logo_x)  if logo_x != ' ' else 0,
            'logo_y' : float(logo_y)  if logo_y != ' ' else 0
        }

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

    def draw_logo(self):
        if self.logo['logo'] not in (None, ''):
            self.c.scale(1, -1)
            x_margin = self.logo['logo_x'] * cm
            y_margin = self.logo['logo_y'] * cm
            w = self.logo['logo_width'] * cm
            h = self.logo['logo_height'] * cm
            image = ImageReader(io.BytesIO(self.logo['logo']))
            self.c.drawImage(image, x_margin, -( y_margin+h), width=w, height=h)
            self.c.scale(1, -1)


    def draw_address_block(self):
        self.setFont("Helvetica", 6)
        self.c.drawString(self.x * cm, self.y * cm, f'{self.company["name"]}, {self.company["address"]}, {self.company["pcode"]}-{self.company["city"]}')
        self.setFont("Helvetica", 11)

        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, self.customer['name'])
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, self.customer['address'])
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f'{self.customer["pcode"]} {self.customer["city"]}')

    def draw_company_info(self):
        self.setFont("Helvetica", 8)
        self.c.drawString(self.x * cm, self.y * cm,  self.company['name'])
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, self.company['address'])
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f'{self.company["country"]}-{self.company["pcode"]} {self.company["city"]}')
        if self.company['vat_number'] not in (None, ''):
            self.y += 0.5
            self.c.drawString(self.x * cm, self.y * cm, f"MWST-NR: { self.company['vat_number']}")
        self.y += 1

    def draw_user_info(self):
        self.setFont("Helvetica", 8)
        self.c.drawString(self.x * cm, self.y * cm, f"Sachbearbeiter: {self.company['agent']}")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f"Email: {self.company['email']}")
        self.y += 0.5

        self.c.drawString(self.x * cm, self.y * cm, f"Tel.: {self.company['phone']}")
        self.y += 1.5



    def draw_doc_info(self):
        self.c.drawString(self.x * cm, self.y * cm, f"Datum: {self.doc_date.strftime('%d.%m.%Y')}")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f"Seite: {self.c.getPageNumber()}/{self.max_pages}")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f"Kunden-Nr.: {self.customer['id']}")
    def draw_header(self):
        pass

    def draw_second_page_header(self):
        pass
    def draw_body(self):
        pass

    def draw_footer(self):
        pass

    def increase_y(self, amount):
        self.y += amount

        last_line = ((self.page_height / cm ) - self.footer_size)


        if self.y >=last_line:
            self.y += 0.5

            self.draw_footer()

            self.c.showPage()
            self.y = 2
            self.apply_settings()

            self.draw_second_page_header()












        #

        #
        # return c
    #
    # def draw_second_page_header(self, c, ypos):
    #     return c,ypos







