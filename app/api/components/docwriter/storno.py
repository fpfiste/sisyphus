from reportlab.lib import pagesizes

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
import datetime as dt


class InvoiceCancellationDoc(Document):
    def __init__(self,cancellation_id, cancellation_date, cancellation_time, cancellation_reason, output_path, invoice_id, invoice_date, invoice_conditions, vat, total, currency):
        self.page_size = pagesizes.A4
        super().__init__(cancellation_id, 'cancellation', language='de', output_path=output_path)
        self.cancellation_date = cancellation_date
        self.cancellation_time = cancellation_time
        self.cancellation_reason = cancellation_reason
        self.invoice_id = invoice_id
        self.invoice_date = invoice_date
        self.invoice_conditions = invoice_conditions
        self.vat = vat
        self.total = total
        self.currency = currency
        self.doc_date = dt.date.today()


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




    def draw(self):
        # Creating Canvas

        self.header()



        self.setFont("Helvetica-Bold", 8)

        if self.cancellation_reason not in ('', None):
            self.c.drawString(2 * cm, 13 * cm, f"Storno Grund: {self.cancellation_reason}")

        self.setFont("Helvetica-Bold", 10)
        self.c.drawString(2 * cm, 14.5 * cm, f'Storno: {self.document_id}')

        self.setFont("Helvetica-Bold", 9)
        # c.setLineWidth(0.25)
        self.c.drawString(2 * cm, 16 * cm, "Rechnung-Nr")
        self.c.drawString(5 * cm, 16 * cm, "Datum")
        self.c.drawString(8 * cm, 16 * cm, "Zahlungsbedingungen")
        self.c.drawRightString(15 * cm, 16 * cm, "MWST")
        self.c.drawRightString(17 * cm, 16 * cm, "Currency")
        self.c.drawRightString(19 * cm, 16 * cm, "Total")




        self.c.line(2 * cm, 16.5 * cm, 19 * cm, 16.5 * cm)


        self.setFont("Helvetica", 9)

        self.c.drawString(2 * cm, 17.5 * cm, f"{self.invoice_id}")
        self.c.drawString(5 * cm, 17.5 * cm, f"{self.invoice_date}")
        self.c.drawString(8 * cm, 17.5 * cm, f"{self.invoice_conditions}")
        self.c.drawRightString(15 * cm, 17.5 * cm, f"{self.vat}")
        self.c.drawRightString(17 * cm, 17.5 * cm, f"{self.currency}")
        self.c.drawRightString(19 * cm, 17.5 * cm, f"{self.total}")


        self.c.line(2 * cm, 18.5 * cm, 19 * cm, 18.5 * cm)


        self.c.setFont("Helvetica", 9)



        # Title Section
        # Again Inverting Scale For strings insertion
        page_num = self.c.getPageNumber()
        self.c.drawString(18 * cm, 29 * cm, 'Seite: ' + str(page_num))




        self.c.save()


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