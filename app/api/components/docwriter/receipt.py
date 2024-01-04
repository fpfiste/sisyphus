from reportlab.lib import colors, pagesizes
from reportlab.pdfgen import canvas

from .document import Document
import os
import tempfile
import textwrap
from pdfrw.toreportlab import makerl
from qrbill import QRBill
from reportlab.graphics import renderPDF
from reportlab.lib.units import cm
from svglib.svglib import svg2rlg
from pdfrw import PdfReader, PageMerge
from pdfrw.buildxobj import pagexobj
import locale
import textwrap



class Receipt(Document):
    def __init__(self,sale_id:int, sale_date:str, sale_time:str, sale_description:float, unit:str, amount:str, price:int, currency: str, clearing_type:str, customer_reference:str, output_path:str, language='de'):
        self.page_size = pagesizes.A4

        super().__init__(sale_id, 'Receipt', language=language, output_path=output_path)
        self.sale_date = sale_date
        self.sale_time = sale_time
        self.sale_description = sale_description
        self.unit = unit
        self.amount = amount
        self.price = price
        self.currency = currency
        self.clearing_type = clearing_type
        self.customer_reference = customer_reference
        self.total = 0
        self.positions = []
        self.draw_brake_lines = True
        self.max_pages = 1
        self.footer_size = 4
        self.doc_date = sale_date





    def header(self):

        self.draw_logo()

        self.x = 2
        self.y = 6
        self.draw_company_info()

        self.x = 13
        self.y = 6
        self.draw_address_block()

        self.x = 2
        self.y = 9
        self.draw_user_info()

        self.y = 12
        self.draw_doc_info()


    def draw_position(self):
        self.setFont("Helvetica", 9)
        self.c.drawString(2 * cm, self.y * cm, str(self.sale_date))

        self.setFont("Helvetica-Bold", 9)
        self.c.drawString(5 * cm, self.y * cm, f'Referenz: {self.customer_reference if self.customer_reference != "" else "-"}')
        self.increase_y(0.5)
        self.setFont("Helvetica", 9)

        wrapper = textwrap.TextWrapper(width=50)

        for line in self.sale_description.split('\n'):
            sublines = wrapper.wrap(text=line)
            for line in sublines:
                self.c.drawString(5 * cm, self.y * cm, f'{line}')
                self.increase_y(0.5)
        self.c.drawString(5 * cm, self.y * cm, f'Uhrzeit: {self.sale_time}')
        self.increase_y(0.5)
        self.c.drawString(5 * cm, self.y * cm, f'Abrechnung: {self.clearing_type}')
        self.setFont("Helvetica", 9)
        self.c.drawString(13 * cm, self.y * cm, self.unit)
        self.c.drawRightString(16 * cm, self.y * cm, f"{self.amount}".replace(",", "'"))
        self.c.drawRightString(17.5 * cm, self.y * cm, f"{self.price:,.2f}".replace(",", "'"))
        self.c.drawRightString(19 * cm, self.y * cm, f"{(self.amount* self.price):,.2f}".replace(",", "'"))

        self.increase_y(0.5)






    def draw(self):
        # Creating Canvas


        self.header()

        self.setFont("Helvetica-Bold", 12)
        self.c.drawString(2 * cm, 15 * cm, f'Quittung: {self.document_id}')
        self.setFont("Helvetica", 10)



        self.setFont("Helvetica", 9)
        # c.setLineWidth(0.25)
        self.c.drawString(2 * cm, 16.5 * cm, "Datum")
        self.c.drawString(5 * cm, 16.5 * cm, "Beschreibung")
        self.c.drawString(13 * cm, 16.5 * cm, "Einheit")
        self.c.drawRightString(16 * cm, 16.5 * cm, "Menge")
        self.c.drawRightString(17.5 * cm, 16.5 * cm, "Preis")
        self.c.drawRightString(19 * cm, 16.5 * cm, "Total")

        self.setStrokeColor(colors.lightgrey)
        self.setLineWidth(0.2)
        self.c.line(1.5 * cm, 17 * cm, 19.5 * cm, 17 * cm)

        self.setFont("Helvetica", 9)

        self.y = 18
        self.draw_position()

        self.increase_y(0.5)
        self.setStrokeColor(colors.lightgrey)
        self.setLineWidth(0.2)
        self.c.line(1.5 * cm, self.y * cm, 19.5 * cm, self.y * cm)
        self.c.save()

        return 0


if __name__ == '__main__':

    doc = Invoice(1,  '2023-09-15', 0.077, 30, 'CHF', '', language='de')


    doc.set_logo(logo_path='/home/fabian/Documents/git/sisyphus/app/frontend/static/img/doc_header.jpg', logo_width=190, logo_height=30, logo_x=10, logo_y=0)
    doc.set_customer(10, 'Rändlimäier Gmbh', 'Flurweg 2', '3377', 'Walliswil bei Wangen', 'CH')
    doc.set_creditor( 'Data Dudes',
                          'Zürichstrasse 9',
                          '6004',
                          'Luzern',
                          'CH' ,
                          'Fabian Pfister',
                          'fabian.pfister@data-dudes.ch',
                          '+41 79 957 25 54',
                          'CH56 0023 5235 1118 6040 N',
                          '07AABCS1429B1Z'
                          )

    doc.add_position(
       1,
        '2023-09-15',
        '09:00:00',
        'Server Setup',
        'Hours',
        5,
        ['Fabian Pfister', 'Ramon Pfister'],
        [],
        'Take way longeer than you need'



    )



    doc.draw()