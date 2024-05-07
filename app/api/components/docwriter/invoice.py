from reportlab.lib import colors, pagesizes
from reportlab.pdfgen import canvas

from stdnum.iso7064 import mod_97_10
from stdnum.iso11649 import format
from stdnum.ch import esr
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
    def __init__(self,invoice_id:int, invoice_date:str, invoice_text:str, vat:float, vat_netto:bool, currency:str, account:str, due_days:int, output_path:str, discount=0, language='de', qr_bill:bool = True, qr_ref:bool=True):
        self.page_size = pagesizes.A4

        super().__init__(invoice_id, 'invoice', language=language, output_path=output_path)
        self.invoice_date = invoice_date
        self.vat = vat
        self.vat_netto = vat_netto
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
        self.footer_size = 4
        self.sub_total_1 = 0
        self.print_qr_bill = qr_bill
        self.print_qr_ref = qr_ref


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

        if self.vat_netto:
            self.sub_total_1 += amount * unit_price
            self.discount_absolute = self.sub_total_1 * self.discount
            self.sub_total_2 = self.sub_total_1 - self.discount_absolute
            self.vat_absoulte = self.sub_total_2 * self.vat
            self.sub_total_3 = self.sub_total_2 + self.vat_absoulte
            self.total = self.sub_total_3
            self.net_total = self.sub_total_2

        else:
            self.sub_total_1 += amount * unit_price
            self.discount_absolute = self.sub_total_1 * self.discount
            self.sub_total_2 = self.sub_total_1 - self.discount_absolute
            self.total = self.sub_total_2
            self.vat_absoulte = self.sub_total_2 / (1 + self.vat) * self.vat
            self.net_total = self.sub_total_2 - self.vat_absoulte


    def calc_qr_reference(self):


        number = (str(self.customer['id']) + '0' + str(self.document_id)).zfill(26)
        check_digit = esr.calc_check_digit(number)

        ref = number + check_digit
        print(ref)
        print(esr.is_valid(ref))

        return ref






    def qr_bill(self):

        debtor = {
            'name': self.customer['name'],
            'street': self.customer['address'],
            'pcode': self.customer['pcode'],
            'city': self.customer['city'],
            'country': self.customer['country']

        }
        creditor = {
                'name' : self.company['name'],
                'street': self.company['address'],
                'pcode': self.company['pcode'],
                'city': self.company['city'],
                'country': self.company['country']

        }

        if self.print_qr_ref:
            reference = self.calc_qr_reference()
        else:
            reference = None



        print(f"{self.total:,.2f}")
        bill = QRBill(
            account= self.account,
            creditor=creditor,
            currency=self.currency,
            reference_number= reference,
            additional_information= f'Rechung: {self.document_id}\n Kunde: {self.customer["id"]} ',
            amount= f"{self.total:.2f}",
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


    def draw_doc_info(self):
        self.c.drawString(self.x * cm, self.y * cm, f"Datum: {self.invoice_date.strftime('%d.%m.%Y')}")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm,  f"Kunden-Nr.: {self.customer['id']}")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm,  f"Zahlungsfrist: {self.due_days} Tage")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f"Seite: {self.c.getPageNumber()}/{self.max_pages}")

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





    def draw_second_page_header(self):
        self.setFont("Helvetica", 8)
        self.c.drawString(2 * cm, self.y * cm, f'Rechnung: {self.document_id}')

        self.c.drawString(18 * cm, self.y * cm, f"Seite: {self.c.getPageNumber()}/{self.max_pages}")
        self.increase_y(0.5)
        self.c.drawString(2 * cm, self.y * cm, f'Datum: {self.invoice_date.strftime("%d.%m.%Y")}')
        self.increase_y(1)
        self.setStrokeColor(colors.lightgrey)
        self.setLineWidth(0.2)
        self.c.line(1.5 * cm, self.y * cm, 19.5 * cm, self.y * cm)
        self.increase_y(0.5)

    def draw_footer(self):
        self.setFont("Helvetica", 8)
        self.c.line(1.5 * cm, self.y * cm, 19.5 * cm, self.y * cm)
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f"IBAN: {self.account}")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f"Währung: {self.currency}")
        self.y += 0.5
        self.c.drawString(self.x * cm, self.y * cm, f"Zahlungsfrist: {self.due_days} Tage")

    def draw_position(self, position):
        self.increase_y(0.5)
        self.setFont("Helvetica", 9)
        self.c.drawString(2 * cm, self.y * cm, str(position['date']))

        self.setFont("Helvetica-Bold", 9)
        self.c.drawString(5 * cm, self.y * cm, f'Referenz: {position["reference_text"] if position["reference_text"] != "" else "-"}')
        self.increase_y(0.5)
        self.setFont("Helvetica", 9)

        wrapper = textwrap.TextWrapper(width=50)

        for line in position["description"].split('\n'):
            sublines = wrapper.wrap(text=line)
            for line in sublines:
                self.c.drawString(5 * cm, self.y * cm, f'{line}')
                self.increase_y(0.5)

        self.c.drawString(5 * cm, self.y * cm, f'Beleg: {position["pos_type"]}-{position["position_id"]}')

        self.setFont("Helvetica", 9)
        self.c.drawString(13 * cm, self.y * cm, position['unit'])
        self.c.drawRightString(16 * cm, self.y * cm, f"{position['amount']:,.2f}".replace(",", "'"))
        self.c.drawRightString(17.5 * cm, self.y * cm, f"{position['unit_price']:,.2f}".replace(",", "'"))
        self.c.drawRightString(19 * cm, self.y * cm, f"{(position['amount'] * position['unit_price']):,.2f}".replace(",", "'"))

        self.increase_y(0.5)


    def draw_totals(self):
        self.setFont("Helvetica", 9)

        self.setStrokeColor(colors.lightgrey)
        self.setLineWidth(0.2)

        self.c.line(1.5 * cm, self.y * cm, 19.5 * cm, self.y * cm)
        self.increase_y(1)

        self.c.drawString(13 * cm, self.y * cm, f'Sub-Total')
        self.c.drawString(16 * cm, self.y * cm, f'{self.currency}')
        self.c.drawRightString(19 * cm, self.y * cm, f"{self.sub_total_1:,.2f}".replace(",", "'"))

        self.increase_y(0.5)
        # c.drawString(12.5 * cm, ypos * cm, 'MWST')

        if self.discount > 0 and self.discount != None:
            self.c.drawString(13 * cm, self.y * cm, f'Rabatt ({(self.discount * 100):.1f}%)')
            self.c.drawString(16 * cm, self.y * cm, f'{self.currency}')
            self.c.drawRightString(19 * cm, self.y * cm, f"{(self.discount_absolute):,.2f}".replace(",", "'"))
            self.increase_y(0.5)

        self.setFont("Helvetica-Bold", 9)
        title = 'Total (exkl. MWST)' if self.vat_netto else f'Total (inkl. MWST)'
        self.c.drawString(13 * cm, self.y * cm, title)
        self.c.drawString(16 * cm, self.y * cm, f'{self.currency}')
        self.c.drawRightString(19 * cm, self.y * cm, f"{self.sub_total_2:,.2f}".replace(",", "'"))
        self.increase_y(0.5)

        self.setFont("Helvetica", 9)
        title = f'MWST ({(self.vat * 100):.1f}%)'
        self.c.drawString(13 * cm, self.y * cm, title)
        self.c.drawString(16 * cm, self.y * cm, f'{self.currency}')
        self.c.drawRightString(19 * cm, self.y * cm, f"{(self.vat_absoulte):,.2f}".replace(",", "'"))
        self.increase_y(0.5)

        if self.vat_netto:
            self.setFont("Helvetica-Bold", 9)
            self.c.drawString(13 * cm, self.y * cm, f'Total')
            self.c.drawString(16 * cm, self.y * cm, f'{self.currency}')
            self.c.drawRightString(19 * cm, self.y * cm, f"{self.sub_total_3:,.2f}".replace(",", "'"))



            self.increase_y(0.5)
        self.c.line(13 * cm, self.y * cm, 19 * cm, self.y * cm)
        self.increase_y(0.5)
        self.c.line(13 * cm, self.y * cm, 19 * cm, self.y * cm)


    def get_max_page(self):

        self.y = 17.5
        for position in self.positions:
           self.draw_position(position)

        self.draw_totals()


        # Title Section
        # Again Inverting Scale For strings insertion
        self.max_pages = self.c.getPageNumber()

        self.c = canvas.Canvas(self.file_name, pagesize=self.page_size, bottomup=0)


    def draw(self):
        # Creating Canvas
        self.get_max_page()

        self.header()

        self.setFont("Helvetica-Bold", 12)
        self.c.drawString(2 * cm, 15 * cm, f'Rechnung: {self.document_id}')
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

        self.y = 17.5
        for position in self.positions:
            self.draw_position(position)

        self.draw_totals()



        last_line = ((self.page_height / cm ) - 13)

        if self.print_qr_bill:
            if self.y >=last_line:
                self.c.showPage()
            qrcode = self.qr_bill()
            self.c.translate(10, 800)
            self.c.scale(1, -1)
            page = PdfReader(qrcode, decompress=False).pages[0]

            p = pagexobj(PageMerge().add(page).render())

            self.c.doForm(makerl(self.c, p))
        else:
            self.y = ((self.page_height / cm ) - self.footer_size) + 0.5
            self.draw_footer()

        self.c.save()

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

if __name__ == '__main__':

    customer_nr = '123'
    invoice_nr = '64654'

    print((customer_nr + invoice_nr).zfill(26))