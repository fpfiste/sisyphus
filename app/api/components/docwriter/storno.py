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


class InvoiceCancellationDoc(Document):
    def __init__(self,cancellation_id, cancellation_date, cancellation_time, cancellation_reason, output_path, invoice_id, invoice_date, invoice_conditions, vat, total, currency):
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


    def draw(self):
        # Creating Canvas

        c = self.draw_template()

        c.drawString(2 * cm, 9 * cm, f"Datum: {self.cancellation_date}")
        c.drawString(2 * cm, 9.5 * cm, f"Sachbearbeiter: {self.company['agent']}")
        c.drawString(2 * cm, 10 * cm, f"Email: {self.company['email']}")
        c.drawString(2 * cm, 10.5 * cm, f"Tel.: {self.company['phone']}")



        c.setFont("Helvetica-Bold", 8)

        if self.cancellation_reason not in ('', None):
            c.drawString(2 * cm, 13 * cm, f"Storno Grund: {self.cancellation_reason}")

        c.setFont("Helvetica-Bold", 10)
        c.drawString(2 * cm, 14.5 * cm, f'Storno: {self.document_id}')

        c.setFont("Helvetica-Bold", 9)
        # c.setLineWidth(0.25)
        c.drawString(2 * cm, 16 * cm, "Rechnung-Nr")
        c.drawString(5 * cm, 16 * cm, "Datum")
        c.drawString(8 * cm, 16 * cm, "Zahlungsbedingungen")
        c.drawRightString(15 * cm, 16 * cm, "MWST")
        c.drawRightString(17 * cm, 16 * cm, "Currency")
        c.drawRightString(19 * cm, 16 * cm, "Total")




        c.line(2 * cm, 16.5 * cm, 19 * cm, 16.5 * cm)


        c.setFont("Helvetica", 9)

        c.drawString(2 * cm, 17.5 * cm, f"{self.invoice_id}")
        c.drawString(5 * cm, 17.5 * cm, f"{self.invoice_date}")
        c.drawString(8 * cm, 17.5 * cm, f"{self.invoice_conditions}")
        c.drawRightString(15 * cm, 17.5 * cm, f"{self.vat}")
        c.drawRightString(17 * cm, 17.5 * cm, f"{self.currency}")
        c.drawRightString(19 * cm, 17.5 * cm, f"{self.total}")


        c.line(2 * cm, 18.5 * cm, 19 * cm, 18.5 * cm)


        c.setFont("Helvetica", 9)



        # Title Section
        # Again Inverting Scale For strings insertion
        page_num = c.getPageNumber()
        c.drawString(18 * cm, 29 * cm, 'Seite: ' + str(page_num))




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