import io
import tempfile
import textwrap

import cairosvg
from cairosvg import svg2png
from qrbill import QRBill
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing
from reportlab.lib import pagesizes
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg
import PIL

class Invoice():
    def __init__(self,invoice_id:int, invoice_date:str, vat:float, due_days: int, currency:str, invoice_text:str, language:str):
        self.invoice_id = invoice_id
        self.invoice_date = invoice_date
        self.vat = vat
        self.invoice_text = invoice_text
        self.currency = currency
        self.due_days = due_days
        self.language = language
        self.customer = None
        self.creditor = None
        self.positions = []
        self.net_total = 0
        self.total = 0

    def set_customer(self,  id, name, address, pcode, city, country):
        self.customer = {
            'id' : id,
            'name': name,
            'adress' : address,
            'pcode' : pcode,
            'city' : city,
            'country' : country
        }

    def set_creditor(self, name, address, pcode, city, country, agent, email, phone, account, vat_number):
        self.creditor = {
            'name': name,
            'adress' : address,
            'pcode' : pcode,
            'city' : city,
            'country' : country,
            'agent' : agent,
            'email' : email,
            'phone' : phone,
            'account' : account,
            'vat_number' : vat_number
        }

    def add_position(self, position_id: int, reference_text:str, description:str, unit:str, amount:float, unit_price:float):
        position = {
            'position_id' : position_id,
            'reference_text' : reference_text,
            'description' : description,
            'unit' : unit,
            'amount' : amount,
            'unit_price' : unit_price,
            'total' : amount * unit_price
        }

        self.positions.append(position)
        self.net_total += amount * unit_price
        self.net_total * (1 + self.vat)

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

    def qr_bill(self):

        debtor = {
            'name': self.customer['name'],
            'pcode': self.customer['pcode'],
            'city': self.customer['city'],
            'country': self.customer['country']

        }
        creditor = {
                'name' : self.creditor['name'],
                'pcode': self.creditor['pcode'],
                'city': self.creditor['city'],
                'country': self.creditor['country']

        }


        bill = QRBill(
            account= self.creditor['account'],
            creditor=creditor,
            amount= str(self.total),
            language= self.language,
            debtor= debtor
        )

        print(type(bill))


        with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
            bill.as_svg(temp)
            temp.seek(0)
            drawing = svg2rlg(temp)
            dpi = 72
            drawing.scale(dpi / 72, dpi / 72)
            renderPDF.drawToFile(drawing, "bill.pdf")




        return drawing


    def draw(self):
        # Creating Canvas


        c = canvas.Canvas('invoice.pdf', pagesize=pagesizes.A4, bottomup=0)
        (width, height) = pagesizes.A4

        c.translate(10, 40)

        ## Logo
        c.scale(1, -1)
        #c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
        # Title Section
        # Again Inverting Scale For strings insertion
        c.scale(1, -1)
        # Again Setting the origin back to (0,0) of top-left
        c.translate(-10, -40)

        c.setFont("Helvetica", 11)

        c.drawString(12 * cm, 5 * cm, self.customer['name'])
        c.drawString(12 * cm, 5.5 * cm, self.customer['adress'])
        c.drawString(12 * cm, 6 * cm, self.customer['pcode'])
        c.drawString(13 * cm, 6 * cm,self.customer['city'])

        c.setFont("Helvetica", 8)
        c.drawString(2 * cm, 5 * cm,  self.creditor['name'])
        c.drawString(2 * cm, 5.5 * cm, self.creditor['adress'])
        c.drawString(2 * cm, 6 * cm, f'{self.creditor["country"]}-{self.creditor["pcode"]} {self.creditor["city"]}')
        c.drawString(2 * cm, 6.5 * cm, f"MWST-NR: { self.creditor['vat_number']}")

        c.drawString(2 * cm, 8 * cm, f"Datum: {self.invoice_date}")
        c.drawString(2 * cm, 8.5 * cm, f"Sachbearbeiter: {self.creditor['agent']}")
        c.drawString(2 * cm, 9 * cm, f"Email: {self.creditor['email']}")
        c.drawString(2 * cm, 9.5 * cm, f"Tel.: {self.creditor['phone']}")

        c.drawString(2 * cm, 11 * cm, f"Kunden-Nr.: {self.customer['id']}")
        c.drawString(2 * cm, 11.5 * cm, f"Zahlungsfrist: {self.due_days} Tage")

        c.setFont("Helvetica-Bold", 8)

        c.drawString(2 * cm, 12 * cm, f"Rechnungs-Text: {self.invoice_text}")

        c.setFont("Helvetica-Bold", 10)
        c.drawString(2 * cm, 14.5 * cm, f'Rechnung: {self.invoice_id}')

        c.setFont("Helvetica", 10)
        # c.setLineWidth(0.25)
        c.drawString(2 * cm, 16 * cm, "Datum")
        c.drawString(4 * cm, 16 * cm, "Beschreibung")
        c.drawString(13 * cm, 16 * cm, "Einheit")
        c.drawRightString(16 * cm, 16 * cm, "Menge")
        c.drawRightString(17.5 * cm, 16 * cm, "Preis")
        c.drawRightString(19 * cm, 16 * cm, "Total")

        c.line(2 * cm, 16.5 * cm, 19 * cm, 16.5 * cm)

        c.setFont("Helvetica", 10)

        ypos = 17.5
        for position in self.positions:
            c.setFont("Helvetica", 10)
            c.drawString(2 * cm, ypos * cm, str(position['position_id']))


            c.setFont("Helvetica-Bold", 10)
            c.drawString(4 * cm, ypos * cm, f'Referenz: {position["reference_text"]}')
            ypos = self.addy(ypos, c, 0.5)


            for i in position['description'].split('\n'):
                c.setFont("Helvetica", 8)
                for line in textwrap.wrap(i, 62):
                    c.drawString(4 * cm, ypos * cm, line)
                    ypos = self.addy(ypos, c, 0.5)
            ypos = self.addy(ypos, c, -0.5)
            c.setFont("Helvetica", 10)
            c.drawString(13 * cm, ypos * cm, position['unit'])
            c.drawRightString(16 * cm, ypos * cm, "%.2f" % position["amount"])
            c.drawRightString(17.5 * cm, ypos * cm, "%.2f" % position["unit_price"])
            c.drawRightString(19 * cm, ypos * cm, "%.2f" % (position["amount"] * position["unit_price"]))

            ypos = self.addy(ypos, c, 1)

        c.setFont("Helvetica", 10)

        c.line(2 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos = self.addy(ypos, c, 1)
        c.drawString(13 * cm, ypos * cm, f'Sub-Total {self.currency} {self.net_total}')
        ypos = self.addy(ypos, c, 0.5)
        # c.drawString(12.5 * cm, ypos * cm, 'MWST')

        c.drawString(13 * cm, ypos * cm, f'MWST ({self.vat * 100}%) {self.currency} {self.net_total * self.vat}')

        ypos = self.addy(ypos, c, 0.5)
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos = self.addy(ypos, c, 0.5)
        c.drawString(13 * cm, ypos * cm, f'Total {self.total}')

        ypos += 0.5
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos += 0.1
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)


        # Title Section
        # Again Inverting Scale For strings insertion
        page_num = c.getPageNumber()
        c.drawString(18 * cm, 29 * cm, 'Seite: ' + str(page_num))

        c.showPage()


        d = self.qr_bill()

        c.translate(0, 90)

        ## Logo
        c.scale(1, -1)

        # Again Setting the origin back to (0,0) of top-left


        c.drawImage('bill.pdf', 1, -800, width=600, height=300)

        c.translate(-10, -40)

        #c.scale(-1, 1)

        c.save()


if __name__ == '__main__':

    invoice = Invoice(1,  '2023-09-15', 0.077, 30, 'CHF', '', language='de')

    invoice.set_customer(10, 'Rändlimäier Gmbh', 'Flurweg 2', '3377', 'Walliswil bei Wangen', 'CH')
    invoice.set_creditor( 'Data Dudes',
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

    invoice.add_position(
       1,
        '',
        'Server Setup',
        'Hours',
        15,
        50

    )

    invoice.draw()