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



class Invoice(Document):
    def __init__(self,invoice_id:int, invoice_date:str, invoice_text:str, vat:float, currency:str, account:str, due_days:int, language:str, output_path:str):
        super().__init__(invoice_id, 'invoice', language='de', output_path=output_path)
        self.invoice_date = invoice_date
        self.vat = vat
        self.invoice_text = invoice_text
        self.currency = currency
        self.account = account
        self.due_days = due_days
        self.net_total = 0
        self.total = 0
        self.positions = []
        print(self.vat)

    def add_position(self, position_id: int, date:str,reference_text:str, description:str, unit:str, amount:float, unit_price:float):
        position = {
            'position_id' : position_id,
            'date' : date,
            'reference_text' : reference_text,
            'description' : description,
            'unit' : unit,
            'amount' : amount,
            'unit_price' : unit_price,
            'total' : amount * unit_price
        }

        self.positions.append(position)
        self.net_total += amount * unit_price

        self.total = round(2*(self.net_total * (1 + self.vat)), 1)
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
    def draw(self):
        # Creating Canvas
        c = self.draw_template()

        c.drawString(2 * cm, 9 * cm, f"Datum: {self.invoice_date}")
        c.drawString(2 * cm, 9.5 * cm, f"Sachbearbeiter: {self.company['agent']}")
        c.drawString(2 * cm, 10 * cm, f"Email: {self.company['email']}")
        c.drawString(2 * cm, 10.5 * cm, f"Tel.: {self.company['phone']}")

        c.drawString(2 * cm, 11.5 * cm, f"Kunden-Nr.: {self.customer['id']}")
        c.drawString(2 * cm, 12 * cm, f"Zahlungsfrist: {self.due_days} Tage")

        c.setFont("Helvetica-Bold", 8)

        if self.invoice_text not in ('', None):
            c.drawString(2 * cm, 13 * cm, f"Rechnungs-Text: {self.invoice_text}")

        c.setFont("Helvetica-Bold", 10)
        c.drawString(2 * cm, 14.5 * cm, f'Rechnung: {self.document_id}')

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
            c.drawString(2 * cm, ypos * cm, str(position['date']))

            c.setFont("Helvetica-Bold", 10)
            c.drawString(5 * cm, ypos * cm, f'Auftrag: {position["position_id"] }')
            ypos = self.addy(ypos, c, 0.5)
            c.setFont("Helvetica", 8)
            c.drawString(5 * cm, ypos * cm, f'Beschreibung: {position["description"]}')
            ypos = self.addy(ypos, c, 0.5)

            if position['reference_text'] not in (None, ''):
                c.drawString(5 * cm, ypos * cm, f'Referenz: {position["reference_text"]}')
                ypos = self.addy(ypos, c, 0.5)

            ypos = 17.5
            c.setFont("Helvetica", 10)
            c.drawString(13 * cm, ypos * cm, position['unit'])
            c.drawRightString(16 * cm, ypos * cm, "%.2f" % position["amount"])
            c.drawRightString(17.5 * cm, ypos * cm, "%.2f" % position["unit_price"])
            c.drawRightString(19 * cm, ypos * cm, "%.2f" % (position["amount"] * position["unit_price"]))

            ypos = self.addy(ypos, c, 1)

        c.setFont("Helvetica", 10)

        c.line(2 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos = self.addy(ypos, c, 1)
        c.drawString(13 * cm, ypos * cm, f'Sub-Total {self.currency}')
        c.drawRightString(19 * cm, ypos * cm, "%.2f" % (self.net_total))
        ypos = self.addy(ypos, c, 0.5)
        # c.drawString(12.5 * cm, ypos * cm, 'MWST')

        c.drawString(13 * cm, ypos * cm, f'MWST ({self.vat * 100}%) {self.currency}')
        c.drawRightString(19 * cm, ypos * cm, "%.2f" % (self.net_total * self.vat))

        ypos = self.addy(ypos, c, 0.5)
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos = self.addy(ypos, c, 0.5)
        c.drawString(13 * cm, ypos * cm, f'Total {self.currency}')
        c.drawRightString(19 * cm, ypos * cm, "%.2f" % (self.total))

        ypos += 0.5
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
        ypos += 0.1
        c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)


        # Title Section
        # Again Inverting Scale For strings insertion
        page_num = c.getPageNumber()
        c.drawString(18 * cm, 29 * cm, 'Seite: ' + str(page_num))



        c.showPage()
        qrcode = self.qr_bill()
        c.translate(10, 800)
        c.scale(1, -1)
        page = PdfReader(qrcode, decompress=False).pages[0]

        p = pagexobj(PageMerge().add(page).render())

        c.doForm(makerl(c, p))

        c.save()


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