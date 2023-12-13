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


class Invoice(Document):
    def __init__(self,invoice_id:int, invoice_date:str, invoice_text:str, vat:float, currency:str, account:str, due_days:int, output_path:str, discount=0, language='de'):
        super().__init__(invoice_id, 'invoice', language=language, output_path=output_path)
        self.invoice_date = invoice_date
        self.vat = vat
        self.invoice_text = invoice_text
        self.currency = currency
        self.account = account
        self.discount = discount
        self.due_days = due_days
        self.net_total = 0
        self.total = 0
        self.positions = []
        self.draw_brake_lines = True
        self.max_pages = 1


    def add_position(self, position_id: int, date:str,reference_text:str, description:str, unit:str, amount:float, unit_price:float, pos_type = ''):
        position = {
            'position_id' : position_id,
            'date' : date,
            'reference_text' : reference_text,
            'description' : description,
            'unit' : unit,
            'amount' : amount,
            'unit_price' : unit_price,
            'total' : amount * unit_price,
            'pos_type': pos_type
        }

        self.positions.append(position)
        self.net_total += amount * unit_price
        self.net_minus_discount = self.net_total * (1-self.discount)
        self.total = round(2*(self.net_minus_discount * (1 + self.vat)), 1)
        self.total = self.total / 2


    def qr_bill(self):

        debtor = {
            'name': self.customer['name'],
            'pcode': self.customer['pcode'],
            'city': self.customer['city'],
            'country': self.customer['country']

        }
        creditor = {
                'name' : self.company['name'],
                'pcode': self.company['pcode'],
                'city': self.company['city'],
                'country': self.company['country']

        }

        print(self.total)
        bill = QRBill(
            account= self.account,
            creditor=creditor,
            amount= str(self.total),
            language= self.language,
            debtor= debtor
        )



        with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
            bill.as_svg(temp)
            temp.seek(0)
            drawing = svg2rlg(temp)

            qr_code_name = os.path.join(self.output_path, f'QR-{self.document_id}.pdf')
            renderPDF.drawToFile(drawing, qr_code_name)

            return qr_code_name


    def first_page_header(self, c):
        c.drawString(2 * cm, 9 * cm, f"Datum: {self.invoice_date.strftime('%d.%m.%Y')}")
        c.drawString(2 * cm, 9.5 * cm, f"Sachbearbeiter: {self.company['agent']}")
        c.drawString(2 * cm, 10 * cm, f"Email: {self.company['email']}")
        c.drawString(2 * cm, 10.5 * cm, f"Tel.: {self.company['phone']}")

        c.drawString(2 * cm, 11.5 * cm, f"Kunden-Nr.: {self.customer['id']}")
        c.drawString(2 * cm, 12 * cm, f"Zahlungsfrist: {self.due_days} Tage")
        c.drawString(2 * cm, 12.5 * cm, f"Seite: {c.getPageNumber()}/{self.max_pages}")

        c.setFont("Helvetica-Bold", 8)

        if self.invoice_text not in ('', None):
            c.drawString(2 * cm, 13 * cm, f"Rechnungs-Text: {self.invoice_text}")

        c.setFont("Helvetica-Bold", 10)
        c.drawString(2 * cm, 14.5 * cm, f'Rechnung: {self.document_id}')

        return c

    def draw_second_page_header(self, c, ypos):
        c.setFont("Helvetica", 8)
        c.drawString(2 * cm, ypos * cm, f'Rechnung: {self.document_id}')

        c.drawString(18 * cm, ypos * cm, f"Seite: {c.getPageNumber()}/{self.max_pages}")
        ypos += 0.5
        c.drawString(2 * cm, ypos * cm, f'Datum: {self.invoice_date.strftime("%d.%m.%Y")}')
        ypos +=1
        return c, ypos


    def draw_position(self, c, ypos, position):
        initial_y = ypos
        c.setFont("Helvetica", 9)
        c.drawString(2 * cm, ypos * cm, str(position['date']))

        c.setFont("Helvetica-Bold", 9)
        c.drawString(5 * cm, ypos * cm,
                     f'Referenz: {position["reference_text"] if position["reference_text"] != "" else "-"}')
        ypos = self.addy(ypos, c, 0.5)
        c.setFont("Helvetica", 9)

        wrapper = textwrap.TextWrapper(width=50)

        for line in position["description"].split('\n'):
            sublines = wrapper.wrap(text=line)
            for line in sublines:
                c.drawString(5 * cm, ypos * cm, f'{line}')
                ypos = self.addy(ypos, c, 0.5)

        c.drawString(5 * cm, ypos * cm, f'Beleg: {position["pos_type"]}-{position["position_id"]}')
        ypos = self.addy(ypos, c, 0.5)

        ypos = self.addy(ypos, c, -0.5)
        c.setFont("Helvetica", 9)
        c.drawString(13 * cm, ypos * cm, position['unit'])
        c.drawRightString(16 * cm, ypos * cm, f"{position['amount']:,.2f}".replace(',', ''))
        c.drawRightString(17.5 * cm, ypos * cm, f"{position['unit_price']:,.2f}".replace(',', ''))
        c.drawRightString(19 * cm, ypos * cm, f"{(position['amount'] * position['unit_price']):,.2f}".replace(',', ''))

        ypos = self.addy(ypos, c, 1)

        return c, ypos
    def draw_totals(self, c, ypos):
        c.setFont("Helvetica", 9)

        c.setStrokeColor(colors.lightgrey)
        c.setLineWidth(0.2)

        c.line(1.5 * cm, ypos * cm, 19.5 * cm, ypos * cm)
        ypos = self.addy(ypos, c, 1)
        c.drawString(13 * cm, ypos * cm, f'Sub-Total')
        c.drawString(16 * cm, ypos * cm, f'{self.currency}')
        c.drawRightString(19 * cm, ypos * cm, f"{self.net_total:,.2f}".replace(',', ''))
        ypos = self.addy(ypos, c, 0.5)
        # c.drawString(12.5 * cm, ypos * cm, 'MWST')

        if self.discount > 0 and self.discount != None:
            c.drawString(13 * cm, ypos * cm, f'Rabatt ({(self.discount * 100):.1f}%)')
            c.drawString(16 * cm, ypos * cm, f'{self.currency}')
            c.drawRightString(19 * cm, ypos * cm, f"{(self.net_total * self.discount):,.2f}".replace(',', ''))
            ypos = self.addy(ypos, c, 0.5)

        c.drawString(13 * cm, ypos * cm, f'MWST ({(self.vat * 100):.1f}%)')
        c.drawString(16 * cm, ypos * cm, f'{self.currency}')
        c.drawRightString(19 * cm, ypos * cm, f"{(self.net_minus_discount * self.vat):,.2f}".replace(',', ''))

        ypos = self.addy(ypos, c, 0.5)
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos = self.addy(ypos, c, 0.5)
        c.drawString(13 * cm, ypos * cm, f'Total')
        c.drawString(16 * cm, ypos * cm, f'{self.currency}')
        c.drawRightString(19 * cm, ypos * cm, "%.2f" % (self.total))

        ypos += 0.5
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos += 0.1
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)

        return c, ypos

    def get_max_page(self):
        c = self.draw_template()

        ypos = 17.5
        for position in self.positions:
            c, ypos = self.draw_position(c, ypos, position)

        c, ypos = self.draw_totals(c, ypos)


        # Title Section
        # Again Inverting Scale For strings insertion
        self.max_pages = c.getPageNumber()


    def draw(self):
        # Creating Canvas
        self.get_max_page()

        c = self.draw_template()

        c = self.first_page_header(c)



        c.setFont("Helvetica", 9)
        # c.setLineWidth(0.25)
        c.drawString(2 * cm, 16 * cm, "Datum")
        c.drawString(5 * cm, 16 * cm, "Beschreibung")
        c.drawString(13 * cm, 16 * cm, "Einheit")
        c.drawRightString(16 * cm, 16 * cm, "Menge")
        c.drawRightString(17.5 * cm, 16 * cm, "Preis")
        c.drawRightString(19 * cm, 16 * cm, "Total")

        c.setStrokeColor(colors.lightgrey)
        c.setLineWidth(0.2)
        c.line(1.5 * cm, 16.5 * cm, 19.5 * cm, 16.5 * cm)

        c.setFont("Helvetica", 9)

        ypos = 17.5
        for position in self.positions:
            c, ypos = self.draw_position(c, ypos, position)

        c, ypos = self.draw_totals(c, ypos)


        # Title Section
        # Again Inverting Scale For strings insertion
        self.max_pages = c.getPageNumber()

        w, h = c._pagesize

        last_line = ((h / cm ) - 13)

        if ypos >=last_line:
            c.showPage()
        qrcode = self.qr_bill()
        c.translate(10, 800)
        c.scale(1, -1)
        page = PdfReader(qrcode, decompress=False).pages[0]

        p = pagexobj(PageMerge().add(page).render())

        c.doForm(makerl(c, p))

        c.save()

        return self.net_total, self.total


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