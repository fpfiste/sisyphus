from io import BytesIO

from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


import csv
import io
import os
import tempfile
import textwrap
import datetime as dt
from collections import OrderedDict








class InvoiceDoc():

    def __init__(self, invoice, task_queryset, sales_queryset):
        self.invoice = invoice
        self.task_queryset = task_queryset
        self.sales_queryset = sales_queryset
        self.width, self.height =  A4
        self.buffer = BytesIO()
        self.customer = (list(sales_queryset) + list(task_queryset))[0].fk_project.fk_customer
        self.logo_path = 'app/frontend/static/img/doc_header.jpg'




    def draw(self):


        # Create the PDF object, using the buffer as its "file."
        c = canvas.Canvas(self.buffer)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        c.drawString(100, 100, "Hello world.")

        # Close the PDF object cleanly, and we're done.
        c.showPage()
        c.save()
        self.buffer.seek(0)
        return self.buffer







#
# class DocumentWriter:
#
#     def __init__(self):
#         self.header_img_path =  os.path.join(BASE_DIR, 'static', 'doc_header.jpg')
#         self.page_counter = 0
#     def print_auftrag(self, auftrag):
#
#         filepath = os.path.join(BASE_DIR, 'static', 'files', 'transportauftrag', 'P_TA' + str(auftrag[0].auftragsid) + '.pdf')
#
#         c = canvas.Canvas(filepath, pagesize=pagesizes.A4, bottomup=0)
#
#         # Creating Canvas
#         for i in auftrag:
#             (width, height) = pagesizes.A4
#
#             c.translate(10, 40)
#
#             ## Logo
#             c.scale(1, -1)
#             c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
#             # Title Section
#             # Again Inverting Scale For strings insertion
#             c.scale(1, -1)
#             # Again Setting the origin back to (0,0) of top-left
#             c.translate(-10, -40)
#
#
#
#
#
#
#             c.setFont("Helvetica", 11)
#
#             c.drawString(12*cm, 5*cm, str(i.kundennr.firma))
#             c.drawString(12*cm, 5.5*cm, str(i.kundennr.adresse))
#             c.drawString(12*cm, 6*cm, str(i.kundennr.locationnr.plz))
#             c.drawString(13*cm, 6*cm, str(i.kundennr.locationnr.ort))
#
#             c.setFont("Helvetica", 8)
#             c.drawString(2*cm, 5*cm, "Pfister Transporte AG")
#             c.drawString(2*cm, 5.5*cm, "Heimenhausenstrasse 4")
#             c.drawString(2*cm, 6*cm, "3377 Walliswil bei Wangen")
#             c.drawString(2*cm, 6.5*cm, "MWST-NR : 07AABCS1429B1Z")
#
#
#             c.drawString(2*cm, 9.5*cm, "Datum :")
#             c.drawString(4.5*cm, 9.5*cm, str(dt.date.today().strftime("%d.%m.%Y")))
#             c.drawString(2 * cm, 10 * cm, "Sachbearbeiter :")
#             c.drawString(4.5 * cm, 10 * cm, 'Hans Pfister')
#             c.drawString(2*cm, 10.5*cm, "Email :")
#             c.drawString(4.5  * cm, 10.5 * cm, "disp@pfister-transporte.ch")
#             c.drawString(2*cm, 11*cm, "Tel. :")
#             c.drawString(4.5  * cm, 11 * cm, "+41 32 631 21 88")
#             c.drawString(2*cm, 11.5*cm, "Kunden-Nr. :")
#             c.drawString(4.5  * cm, 11.5 * cm, str(i.kundennr.kundenid))
#
#             if i.fahrzeugnr != None:
#                 c.drawString(2 * cm, 12 * cm, "Fahrzeug :")
#                 c.drawString(4.5 * cm, 12 * cm, str(i.fahrzeugnr.nummernschild))
#             if i.partnernr != None:
#                 c.drawString(2 * cm, 12 * cm, "Spediteur :")
#                 c.drawString(4.5 * cm, 12 * cm, str(i.partnernr.firma))
#             if i.referenz != None:
#                 c.drawString(2 * cm, 12.5 * cm, "Referenz-Nr. :")
#                 c.drawString(4.5 * cm, 12.5 * cm, str(i.referenz))
#
#
#
#             c.setFont("Helvetica-Bold", 10)
#             c.drawString(2*cm, 14 * cm, 'Transportauftrag:')
#             c.drawString(5.5 * cm, 14 * cm, str(i.auftragsid))
#
#             c.setFont("Helvetica", 10)
#            # c.setLineWidth(0.25)
#             c.drawString(2*cm, 15 * cm, "Datum")
#             c.drawString(4*cm, 15 * cm, "Beschreibung")
#             c.drawString(16.5*cm, 15 * cm, "Einheit")
#             c.drawString(18*cm, 15 * cm, "Menge")
#
#             c.line(2*cm, 15.5 * cm, 19*cm, 15.5*cm)
#
#             c.setFont("Helvetica", 10)
#             ypos = 16.5
#             c.drawString(2*cm, ypos * cm, str(i.datefrom.strftime("%d.%m.%Y")))
#             for j in i.beschreibung.split('\n'):
#                 c.setFont("Helvetica", 8)
#                 for line in textwrap.wrap(j, 62):
#                     c.drawString(4 * cm, ypos * cm, line)
#                     ypos = self.addy(ypos, c, 0.5)
#             c.drawString(4*cm, ypos * cm, 'Ladezeit:')
#             c.drawString(6*cm, ypos * cm, str(i.timefrom.strftime('%H:%M')))
#
#             ypos = self.addy(ypos, c, 0.5)
#             c.drawString(4*cm, ypos * cm, 'Abladezeit:')
#             c.drawString(6*cm, ypos * cm, str(i.datefrom.strftime('%d.%m.%Y')) + ' ' + str(i.timeto.strftime('%H:%M')))
#             if i.einheitnr != None:
#                 c.drawString(17*cm, ypos * cm, str(i.einheitnr.einheit))
#             if i.menge != None:
#                 c.drawString(19*cm, ypos * cm, str(i.menge))
#
#             c.drawString(12*cm, 22*cm, 'Unterschrift Warenempfänger **')
#             c.rect(12*cm, 22.5*cm, 5*cm, 3*cm, fill=0)
#
#             c.setFont("Helvetica", 6)
#             c.drawString(2*cm, 28*cm, '** Mit Ihrer Unterschrift bestätigen Sie den kompletten Erhalt der Ware gemäss Vereinbarung. Zudem besätigen Sie dass die Ware ohne jegliche Mängel überliefert wurde.')
#             c.showPage()
#
#
#
#
#         c.save()
#         return '/static/files/transportauftrag/P_TA' + str(auftrag[0].auftragsid) + '.pdf'
#
#     def write_quittung(self, auftrag, beschreibung):
#         # Creating Canvas
#
#         title = 'Quittung Waschanlage'
#
#
#         c = canvas.Canvas(self.buffer, pagesize=pagesizes.A4, bottomup=0)
#         (width, height) = pagesizes.A4
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#
#
#
#
#
#         c.setFont("Helvetica", 11)
#
#         c.drawString(12*cm, 5*cm, str(auftrag.kundennr.firma))
#         c.drawString(12*cm, 5.5*cm, str(auftrag.kundennr.adresse))
#         c.drawString(12*cm, 6*cm, str(auftrag.kundennr.locationnr.plz))
#         c.drawString(13*cm, 6*cm, str(auftrag.kundennr.locationnr.ort))
#
#         c.setFont("Helvetica", 8)
#         c.drawString(2*cm, 5*cm, "Pfister Transporte AG")
#         c.drawString(2*cm, 5.5*cm, "Heimenhausenstrasse 4")
#         c.drawString(2*cm, 6*cm, "3377 Walliswil bei Wangen")
#         c.drawString(2*cm, 6.5*cm, "MWST-NR : 07AABCS1429B1Z")
#
#
#         c.drawString(2*cm, 9.5*cm, "Datum :")
#         c.drawString(4.5*cm, 9.5*cm, str(date.today().strftime("%d.%m.%Y")))
#         c.drawString(2 * cm, 10 * cm, "Sachbearbeiter :")
#         c.drawString(4.5 * cm, 10 * cm, 'Hans Pfister')
#         c.drawString(2*cm, 10.5*cm, "Email :")
#         c.drawString(4.5  * cm, 10.5 * cm, "disp@pfister-transporte.ch")
#         c.drawString(2*cm, 11*cm, "Tel. :")
#         c.drawString(4.5  * cm, 11 * cm, "+41 32 631 21 88")
#
#
#         c.setFont("Helvetica-Bold", 11)
#         c.drawString(2*cm, 14 * cm, title)
#
#
#         c.setFont("Helvetica", 11)
#        # c.setLineWidth(0.25)
#         c.drawString(2*cm, 15 * cm, "Datum")
#         c.drawString(4*cm, 15 * cm, "Beschreibung")
#         c.drawString(10*cm, 15 * cm, "Einheit")
#         c.drawString(12*cm, 15 * cm, "Menge")
#         c.drawCentredString(15*cm, 15 * cm, "Preis")
#         c.drawCentredString(17*cm, 15 * cm, "Total")
#
#         c.line(2*cm, 15.5 * cm, 18.5*cm, 15.5*cm)
#
#         c.setFont("Helvetica", 10)
#         c.drawString(2*cm, 16.5 * cm, str(auftrag.date.strftime("%d.%m.%Y")))
#         c.drawString(4*cm, 16.5 * cm, str(beschreibung))
#         c.drawString(10*cm, 16.5 * cm, str(auftrag.einheitnr.einheit))
#         c.drawString(12*cm, 16.5 * cm, str(auftrag.menge))
#         c.drawCentredString(15*cm, 16.5 * cm, str(auftrag.preis))
#         c.drawCentredString(17*cm, 16.5 * cm, str(auftrag.menge * auftrag.preis))
#
#         c.drawString(12*cm, 22*cm, 'Unterschrift Kunde **')
#         c.rect(12*cm, 22.5*cm, 5*cm, 3*cm, fill=0)
#
#         c.setFont("Helvetica", 6)
#         c.drawString(2*cm, 28*cm, '** Mit Ihrer Unterschrift bestätigen Sie den kompletten Erhalt der Ware gemäss Vereinbarung. Zudem besätigen Sie dass die Ware ohne jegliche Mängel überliefert wurde.')
#
#
#
#
#         c.save()
#         self.buffer.seek(0)
#         return self.buffer
#
#     def write_invoice(self, queryset):
#
#         # Creating Canvas
#         auftrag = queryset[0]
#         title = 'Rechnung:'
#         rechnungsnr = str(auftrag.rechnungsnr.rechnungsid)
#
#         filepath = os.path.join(BASE_DIR, 'static', 'files', 'invoices',  'RG' + rechnungsnr + '.pdf')
#
#
#         c = canvas.Canvas(filepath, pagesize=pagesizes.A4, bottomup=0)
#         (width, height) = pagesizes.A4
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#
#         c.setFont("Helvetica", 11)
#
#         c.drawString(12*cm, 5*cm, str(auftrag.kundennr.firma))
#         c.drawString(12*cm, 5.5*cm, str(auftrag.kundennr.adresse))
#         c.drawString(12*cm, 6*cm, str(auftrag.kundennr.locationnr.plz))
#         c.drawString(13*cm, 6*cm, str(auftrag.kundennr.locationnr.ort))
#
#         c.setFont("Helvetica", 8)
#         c.drawString(2*cm, 5*cm, "Pfister Transporte AG")
#         c.drawString(2*cm, 5.5*cm, "Heimenhausenstrasse 4")
#         c.drawString(2*cm, 6*cm, "3377 Walliswil bei Wangen")
#         c.drawString(2*cm, 6.5*cm, "MWST-NR : 07AABCS1429B1Z")
#
#
#         c.drawString(2*cm, 8*cm, "Datum :")
#         c.drawString(4.5*cm, 8*cm, auftrag.rechnungsnr.date.strftime("%d.%m.%Y"))
#         c.drawString(2 * cm, 8.5 * cm, "Sachbearbeiter :")
#         c.drawString(4.5 * cm, 8.5 * cm, 'Hans Pfister')
#         c.drawString(2*cm, 9*cm, "Email :")
#         c.drawString(4.5  * cm, 9 * cm, "dispo@pfister-transporte.ch")
#         c.drawString(2*cm, 9.5*cm, "Tel. :")
#         c.drawString(4.5  * cm, 9.5 * cm, "+41 32 631 21 88")
#
#         c.drawString(2*cm, 11*cm, "Kunden-Nr. :")
#         c.drawString(4.5  * cm, 11 * cm, str(auftrag.kundennr.kundenid))
#         c.drawString(2*cm, 11.5*cm, "Zahlungsfrist: ")
#         c.drawString(4.5  * cm, 11.5 * cm, '30 Tage')
#         c.setFont("Helvetica-Bold", 8)
#         if auftrag.kundennr.rechnungstext not in ('', None):
#             c.drawString(2*cm, 12*cm, "Rechnungs-Text :")
#             c.drawString(4.5  * cm, 12 * cm, str(auftrag.kundennr.rechnungstext))
#
#
#
#         c.setFont("Helvetica-Bold", 10)
#         c.drawString(2*cm, 14.5 * cm, title)
#         c.drawString(5.5 * cm, 14.5* cm, rechnungsnr)
#
#         c.setFont("Helvetica", 10)
#        # c.setLineWidth(0.25)
#         c.drawString(2*cm, 16 * cm, "Datum")
#         c.drawString(4*cm, 16 * cm, "Beschreibung")
#         c.drawString(13*cm, 16 * cm, "Einheit")
#         c.drawRightString(16*cm, 16 * cm, "Menge")
#         c.drawRightString(17.5*cm, 16 * cm, "Preis")
#         c.drawRightString(19*cm, 16 * cm, "Total")
#
#
#         c.line(2*cm, 16.5 * cm, 19*cm, 16.5*cm)
#
#         c.setFont("Helvetica", 10)
#
#         ypos = 17.5
#         sub_total = 0
#         for auftrag in queryset:
#             c.setFont("Helvetica", 10)
#             c.drawString(2*cm, ypos * cm, str(auftrag.datefrom.strftime("%d.%m.%Y")))
#
#             if auftrag.referenz not in ('', None):
#                 c.setFont("Helvetica-Bold", 10)
#                 c.drawString(4*cm, ypos * cm, 'Referenz: ')
#                 c.drawString(6*cm, ypos * cm, str(auftrag.referenz))
#                 ypos = self.addy(ypos, c, 0.5)
#
#             c.drawString(4 * cm, ypos * cm, 'Auftrag-Nr: ')
#             c.drawString(6 * cm, ypos * cm, str(auftrag.auftragsid))
#             ypos = self.addy(ypos, c, 0.5)
#
#             for i in auftrag.beschreibung.split('\n'):
#                 c.setFont("Helvetica", 8)
#                 for line in textwrap.wrap(i, 62):
#                     c.drawString(4 * cm, ypos * cm, line)
#                     ypos = self.addy(ypos, c, 0.5)
#             if auftrag.fahrzeugnr not in ('', None):
#                 c.setFont("Helvetica", 8)
#                 c.drawString(4 * cm, ypos * cm, 'Nummernschild: ')
#                 c.drawString(6.5 * cm, ypos * cm, str(auftrag.fahrzeugnr.nummernschild))
#                 ypos = self.addy(ypos, c, 0.5)
#
#
#
#             ypos = self.addy(ypos, c, -0.5)
#             c.setFont("Helvetica", 10)
#             c.drawString(13*cm, ypos * cm, str(auftrag.einheitnr.einheit))
#             c.drawRightString(16*cm, ypos * cm, "%.2f" % auftrag.menge)
#             c.drawRightString(17.5*cm, ypos * cm,  "%.2f" % auftrag.preis)
#             c.drawRightString(19*cm, ypos * cm, "%.2f" % (auftrag.menge * auftrag.preis))
#             sub_total += auftrag.menge * auftrag.preis
#             ypos = self.addy(ypos, c, 1)
#
#         c.setFont("Helvetica", 10)
#
#         c.line(2 * cm, ypos * cm, 19 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 1)
#         c.drawString(13 * cm, ypos * cm, 'Sub-Total')
#         c.drawString(16 * cm, ypos * cm, auftrag.currencynr.currency)
#         c.drawRightString(19 * cm, ypos * cm, "%.2f" % sub_total)
#         ypos = self.addy(ypos, c, 0.5)
#         #c.drawString(12.5 * cm, ypos * cm, 'MWST')
#         if auftrag.export_import == 1:
#             mwst = 0
#             c.drawString(13 * cm, ypos * cm, 'MWST (0.0%)')
#
#             c.drawString(16 * cm, ypos * cm, auftrag.currencynr.currency)
#             c.drawRightString(19 * cm, ypos * cm, '0.00')
#         else:
#             mwst = 0.077
#             c.drawString(13 * cm, ypos * cm, 'MWST (7.7%)')
#             c.drawString(16 * cm, ypos * cm, auftrag.currencynr.currency)
#             c.drawRightString(19 * cm, ypos * cm, "%.2f" % round((sub_total * mwst),2))
#
#         ypos = self.addy(ypos, c, 0.5)
#         c.line(13* cm, ypos * cm, 19 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(13 * cm, ypos * cm, 'Total')
#         c.drawString(16 * cm, ypos * cm, auftrag.currencynr.currency)
#         total = round(2*(sub_total * (1+mwst)), 1)
#         total = total / 2
#         c.drawRightString(19 * cm, ypos * cm, "%.2f" % total)
#         ypos += 0.5
#         c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
#         ypos += 0.1
#         c.line(13 * cm, ypos * cm, 19 * cm, ypos * cm)
#
#         if auftrag.currencynr.currency == 'CHF':
#             account = ACCOUNT_CHF
#         elif auftrag.currencynr.currency == 'EUR':
#             account = ACCOUNT_EUR
#
#         ## Logo
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         page_num = c.getPageNumber()
#         c.drawString(18 * cm, 29 * cm, 'Seite: ' + str(page_num))
#
#         c.showPage()
#         qrbill = self.generate_qr_bill(rechnungsnr= auftrag.rechnungsnr.rechnungsid,
#                                         customer_name=auftrag.kundennr.firma,
#                                        customer_plz= auftrag.kundennr.locationnr.plz,
#                                        cusotmer_city= auftrag.kundennr.locationnr.ort,
#                                        customer_country= 'CH',
#                                        account= str(account),
#                                        language= 'de',
#                                        amount=total)
#
#
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(qrbill, 1, -800, width=600, height=300)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#       # Again Setting the origin back to (0,0) of top-left
#       #   c.saveState()
#       #   renderPDF.draw(qrbill, c, 50,50)
#       #   c.restoreState()
#
#         ## Logo
#
#
#         # Again Setting the origin back to (0,0) of top-left
#
#
#         c.save()
#
#
#
#         # filename = os.path.join(BASE_DIR, 'files', 'invoices', 'RG_' + str(rechnungsnr) + '.pdf')
#         # with open(filename, 'wb') as file:
#         #     file.write(self.buffer.read())
#
#         return ('/static/files/invoices/RG' + rechnungsnr + '.pdf', total, mwst)
#
#     def write_tankstellen_invoice(self, rechnung, queryset):
#
#         # Creating Canvas
#         title = 'Rechnung:'
#         rechnungsnr = str(rechnung.rechnungsid)
#         kunde = queryset[0].kundennr
#
#         filepath = os.path.join(BASE_DIR, 'static', 'files', 'invoices',  'RG' + rechnungsnr + '.pdf')
#
#         c = canvas.Canvas(filepath, pagesize=pagesizes.A4, bottomup=0)
#         (width, height) = pagesizes.A4
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#         c.setFont("Helvetica", 11)
#
#         c.drawString(12*cm, 5*cm, str(kunde.firma))
#         c.drawString(12*cm, 5.5*cm, str(kunde.adresse))
#         c.drawString(12*cm, 6*cm, str(kunde.locationnr.plz))
#         c.drawString(13*cm, 6*cm, str(kunde.locationnr.ort))
#
#         c.setFont("Helvetica", 8)
#         c.drawString(2*cm, 5*cm, "Pfister Transporte AG")
#         c.drawString(2*cm, 5.5*cm, "Heimenhausenstrasse 4")
#         c.drawString(2*cm, 6*cm, "3377 Walliswil bei Wangen")
#         c.drawString(2*cm, 6.5*cm, "MWST-NR : 07AABCS1429B1Z")
#
#
#         c.drawString(2*cm, 9.5*cm, "Datum :")
#         c.drawString(4.5*cm, 9.5*cm, rechnung.date.strftime("%d.%m.%Y"))
#         c.drawString(2 * cm, 10 * cm, "Sachbearbeiter :")
#         c.drawString(4.5 * cm, 10 * cm, 'Hans Pfister')
#         c.drawString(2*cm, 10.5*cm, "Email :")
#         c.drawString(4.5  * cm, 10.5 * cm, "disp@pfister-transporte.ch")
#         c.drawString(2*cm, 11*cm, "Tel. :")
#         c.drawString(4.5  * cm, 11 * cm, "+41 32 631 21 88")
#
#         c.setFont("Helvetica-Bold", 11)
#         c.drawString(2*cm, 14 * cm, title)
#         c.drawString(5.5 * cm, 14 * cm, rechnungsnr)
#
#         c.setFont("Helvetica", 11)
#        # c.setLineWidth(0.25)
#         c.drawString(2*cm, 15 * cm, "Datum")
#         c.drawString(4 * cm, 15 * cm, "Referenz")
#         c.drawString(6*cm, 15 * cm, "Beschreibung")
#         c.drawString(10*cm, 15 * cm, "Einheit")
#         c.drawString(12*cm, 15 * cm, "Menge")
#         c.drawString(15*cm, 15 * cm, "Preis")
#         c.drawString(17*cm, 15 * cm, "Total")
#
#         c.line(2*cm, 15.5 * cm, 18*cm, 15.5*cm)
#
#         c.setFont("Helvetica", 10)
#
#         ypos = 16.5
#         sub_total = 0
#         for bezug in queryset.filter(bezugtyp = 1):
#             c.drawString(2*cm, ypos * cm, str(bezug.bezugdate.strftime("%d.%m.%Y")))
#             c.drawString(4 * cm, ypos * cm, str(bezug.schlüsselnr.keyid))
#             c.drawString(6 * cm, ypos * cm, 'Dieselbezug')
#             c.drawString(10*cm, ypos * cm, str(bezug.einheitnr.einheit))
#             c.drawString(12*cm, ypos * cm, str(bezug.menge))
#             c.drawString(15*cm, ypos * cm, str(bezug.preis))
#             c.drawRightString(17*cm, ypos * cm, '{:.2f}'.format(round(bezug.menge * bezug.preis , 2)))
#             sub_total += round(bezug.menge * bezug.preis * 2, 1) / 2
#             ypos = self.addy(ypos, c, 0.5)
#         ypos = self.addy(ypos, c, 0.5)
#
#         for bezug in queryset.filter(bezugtyp = 2):
#             c.drawString(2*cm, ypos * cm, str(bezug.bezugdate.strftime("%d.%m.%Y")))
#             c.drawString(4 * cm, ypos * cm, str(bezug.text))
#             c.drawString(6 * cm, ypos * cm, 'Waschen')
#             c.drawString(10*cm, ypos * cm, str(bezug.einheitnr.einheit))
#             c.drawString(12*cm, ypos * cm, str(bezug.menge))
#             c.drawString(15*cm, ypos * cm, str(bezug.preis))
#             c.drawRightString(17*cm, ypos * cm,'{:.2f}'.format(round(bezug.menge * bezug.preis , 2)))
#             sub_total += round(bezug.menge * bezug.preis * 2, 1) / 2
#             ypos = self.addy(ypos, c, 0.5)
#
#         ypos = self.addy(ypos, c, 0.5)
#
#         for bezug in queryset.filter(bezugtyp = 3):
#             c.drawString(2 * cm, ypos * cm, str(bezug.bezugdate.strftime("%d.%m.%Y")))
#             c.drawString(4 * cm, ypos * cm, str(bezug.text))
#             c.drawString(6 * cm, ypos * cm, 'AdBlue')
#             c.drawString(10 * cm, ypos * cm, str(bezug.einheitnr.einheit))
#             c.drawString(12 * cm, ypos * cm, str(bezug.menge))
#             c.drawString(15 * cm, ypos * cm, str(bezug.preis))
#             c.drawRightString(17 * cm, ypos * cm, '{:.2f}'.format(round(bezug.menge * bezug.preis , 2)))
#             sub_total += round(bezug.menge * bezug.preis * 2, 1) / 2
#             ypos = self.addy(ypos, c, 0.5)
#
#         c.setFont("Helvetica", 10)
#
#         ypos = self.addy(ypos, c, 0.5)
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'Sub-Total')
#         c.drawString(15 * cm, ypos * cm, 'CHF')
#         c.drawRightString(17 * cm, ypos * cm, '{:.2f}'.format(sub_total))
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'MWST')
#
#         mwst = 0.077
#         c.drawString(12 * cm, ypos * cm, 'MWST (7.7%)')
#         c.drawString(15 * cm, ypos * cm, 'CHF')
#         c.drawRightString(17 * cm, ypos * cm, '{:.2f}'.format(round(sub_total / 100 * 7.7,2)))
#
#         ypos = self.addy(ypos, c, 0.5)
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'Total')
#         c.drawString(15 * cm, ypos * cm, 'CHF')
#         total = round(2*(sub_total * (1+mwst)), 1)
#         total = total / 2
#         c.drawRightString(17 * cm, ypos * cm, '{:.2f}'.format(total))
#         ypos += 0.5
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos += 0.1
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#
#         account = ACCOUNT_CHF
#         ## Logo
#         # Title Section
#         # Again Inverting Scale For strings insertion
#
#         c.showPage()
#         qrbill = self.generate_qr_bill(rechnungsnr= rechnung.rechnungsid,
#                                         customer_name=kunde.firma,
#                                        customer_plz= kunde.locationnr.plz,
#                                        cusotmer_city= kunde.locationnr.ort,
#                                        customer_country= 'CH',
#                                        account= str(account),
#                                        language= 'de',
#                                        amount=total)
#
#
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(qrbill, 1, -800, width=600, height=300)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#         c.save()
#
#         return ('/static/files/invoices/RG' + rechnungsnr + '.pdf', total, mwst)
#
#     def write_div_invoice(self, rechnung, queryset):
#         bezug = queryset[0]
#         kunde = queryset[0].kundennr
#
#         # Creating Canvas
#         title = 'Rechnung:'
#         rechnungsnr = str(rechnung.rechnungsid)
#         filename = 'RG' + rechnungsnr + '.pdf'
#
#         c = canvas.Canvas(self.buffer, pagesize=pagesizes.A4, bottomup=0)
#         (width, height) = pagesizes.A4
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#
#
#
#
#
#         c.setFont("Helvetica", 11)
#
#         c.drawString(12*cm, 5*cm, str(kunde.firma))
#         c.drawString(12*cm, 5.5*cm, str(kunde.adresse))
#         c.drawString(12*cm, 6*cm, str(kunde.locationnr.plz))
#         c.drawString(13*cm, 6*cm, str(kunde.locationnr.ort))
#
#         c.setFont("Helvetica", 8)
#         c.drawString(2*cm, 5*cm, "Pfister Transporte AG")
#         c.drawString(2*cm, 5.5*cm, "Heimenhausenstrasse 4")
#         c.drawString(2*cm, 6*cm, "3377 Walliswil bei Wangen")
#         c.drawString(2*cm, 6.5*cm, "MWST-NR : 07AABCS1429B1Z")
#
#
#         c.drawString(2*cm, 9.5*cm, "Datum :")
#         c.drawString(4.5*cm, 9.5*cm, rechnung.date.strftime("%d.%m.%Y"))
#         c.drawString(2 * cm, 10 * cm, "Sachbearbeiter :")
#         c.drawString(4.5 * cm, 10 * cm, 'Hans Pfister')
#         c.drawString(2*cm, 10.5*cm, "Email :")
#         c.drawString(4.5  * cm, 10.5 * cm, "disp@pfister-transporte.ch")
#         c.drawString(2*cm, 11*cm, "Tel. :")
#         c.drawString(4.5  * cm, 11 * cm, "+41 32 631 21 88")
#
#
#
#
#         c.setFont("Helvetica-Bold", 11)
#         c.drawString(2*cm, 14 * cm, title)
#         c.drawString(5.5 * cm, 14 * cm, rechnungsnr)
#
#         c.setFont("Helvetica", 11)
#        # c.setLineWidth(0.25)
#         c.drawString(2*cm, 15 * cm, "Datum")
#         c.drawString(4 * cm, 15 * cm, "Referenz")
#         c.drawString(6*cm, 15 * cm, "Beschreibung")
#         c.drawString(10*cm, 15 * cm, "Einheit")
#         c.drawString(12*cm, 15 * cm, "Menge")
#         c.drawString(15*cm, 15 * cm, "Preis")
#         c.drawString(17*cm, 15 * cm, "Total")
#
#
#         c.line(2*cm, 15.5 * cm, 18.5*cm, 15.5*cm)
#
#         c.setFont("Helvetica", 10)
#
#         ypos = 16.5
#         sub_total = 0
#         for bezug in queryset:
#             c.drawString(2*cm, ypos * cm, str(bezug.datum.strftime("%d.%m.%Y")))
#             c.drawString(4 * cm, ypos * cm, str(bezug.beschreibung))
#             c.drawString(6 * cm, ypos * cm,  str(bezug.einheitnr.einheit))
#             c.drawString(10*cm, ypos * cm, str(bezug.menge))
#             c.drawString(12*cm, ypos * cm, str(bezug.preis))
#             c.drawRightString(17*cm, ypos * cm, '{:.2f}'.format(round(bezug.menge * bezug.preis , 2)))
#             sub_total += round(bezug.menge * bezug.preis * 2, 1) / 2
#             ypos = self.addy(ypos, c, 0.5)
#         ypos = self.addy(ypos, c, 0.5)
#
#
#
#         c.setFont("Helvetica", 10)
#
#         ypos = self.addy(ypos, c, 0.5)
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'Sub-Total')
#         c.drawString(15 * cm, ypos * cm, 'CHF')
#         c.drawRightString(17 * cm, ypos * cm, '{:.2f}'.format(sub_total))
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'MWST')
#
#         mwst = 0.077
#         c.drawString(12 * cm, ypos * cm, 'MWST (7.7%)')
#         c.drawString(15 * cm, ypos * cm, 'CHF')
#         c.drawRightString(17 * cm, ypos * cm, '{:.2f}'.format(round(sub_total / 100 * 7.7,2)))
#
#         ypos = self.addy(ypos, c, 0.5)
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'Total')
#         c.drawString(15 * cm, ypos * cm, 'CHF')
#         total = round(2*(sub_total * (1+mwst)), 1)
#         total = total / 2
#         c.drawRightString(17 * cm, ypos * cm, '{:.2f}'.format(total))
#         ypos += 0.5
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos += 0.1
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#
#         account = ACCOUNT_CHF
#         ## Logo
#         # Title Section
#         # Again Inverting Scale For strings insertion
#
#         c.showPage()
#         qrbill = self.generate_qr_bill(rechnungsnr= rechnung.rechnungsid,
#                                         customer_name=kunde.firma,
#                                        customer_plz= kunde.locationnr.plz,
#                                        cusotmer_city= kunde.locationnr.ort,
#                                        customer_country= 'CH',
#                                        account= str(account),
#                                        language= 'de',
#                                        amount=total)
#
#
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(qrbill, 1, -800, width=600, height=300)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#       # Again Setting the origin back to (0,0) of top-left
#       #   c.saveState()
#       #   renderPDF.draw(qrbill, c, 50,50)
#       #   c.restoreState()
#
#         ## Logo
#
#
#         # Again Setting the origin back to (0,0) of top-left
#
#
#         c.save()
#         self.buffer.seek(0)
#         #
#         # filename = os.path.join(BASE_DIR, 'files', 'invoices', 'RG_' + str(rechnungsnr) + '.pdf')
#         # with open(filename, 'wb') as file:
#         #     file.write(self.buffer.read())
#
#         return (self.buffer, total, kunde)
#     def write_storno(self, storno):
#
#         kunde = storno.rechnungsnr.kundennr
#         # Creating Canvas
#         title = 'Storno:'
#         stornonr = str(storno.stornoid)
#
#         filename = os.path.join(BASE_DIR,'static', 'files', 'stornos', 'ST_' + str(stornonr) + '.pdf')
#
#         c = canvas.Canvas(filename, pagesize=pagesizes.A4, bottomup=0)
#         (width, height) = pagesizes.A4
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#         c.setFont("Helvetica", 11)
#
#         c.drawString(12*cm, 5*cm, str(kunde.firma))
#         c.drawString(12*cm, 5.5*cm, str(kunde.adresse))
#         c.drawString(12*cm, 6*cm, str(kunde.locationnr.plz))
#         c.drawString(13*cm, 6*cm, str(kunde.locationnr.ort))
#
#         c.setFont("Helvetica", 8)
#         c.drawString(2*cm, 5*cm, "Pfister Transporte AG")
#         c.drawString(2*cm, 5.5*cm, "Heimenhausenstrasse 4")
#         c.drawString(2*cm, 6*cm, "3377 Walliswil bei Wangen")
#         c.drawString(2*cm, 6.5*cm, "MWST-NR : 07AABCS1429B1Z")
#
#
#         c.drawString(2*cm, 9.5*cm, "Datum :")
#         c.drawString(4.5*cm, 9.5*cm, storno.date.strftime("%d.%m.%Y"))
#         c.drawString(2 * cm, 10 * cm, "Sachbearbeiter :")
#         c.drawString(4.5 * cm, 10 * cm, 'Hans Pfister')
#         c.drawString(2*cm, 10.5*cm, "Email :")
#         c.drawString(4.5  * cm, 10.5 * cm, "disp@pfister-transporte.ch")
#         c.drawString(2*cm, 11*cm, "Tel. :")
#         c.drawString(4.5  * cm, 11 * cm, "+41 32 631 21 88")
#
#         c.setFont("Helvetica-Bold", 11)
#         c.drawString(2*cm, 14 * cm, title)
#         c.drawString(5.5 * cm, 14 * cm, stornonr)
#
#         c.setFont("Helvetica", 10)
#        # c.setLineWidth(0.25)
#         c.drawString(2*cm, 15 * cm, "Rechnung")
#         c.drawString(4 * cm, 15 * cm, "Datum")
#         c.drawString(6*cm, 15 * cm, "Beschreibung")
#         c.drawString(9*cm, 15 * cm, "Kunde")
#         c.drawString(15*cm, 15 * cm, "MWST")
#         c.drawString(17*cm, 15 * cm, "Total")
#
#
#         c.line(2*cm, 15.5 * cm, 18.5*cm, 15.5*cm)
#
#         c.setFont("Helvetica", 10)
#
#         ypos = 16.5
#
#
#         c.drawString(2*cm, ypos * cm, str(storno.rechnungsnr.rechnungsid))
#         c.drawString(4 * cm, ypos * cm,  str(storno.rechnungsnr.date.strftime("%d.%m.%Y")))
#         c.drawString(6 * cm, ypos * cm, str(storno.rechnungsnr.typnr.typ))
#         c.drawString(9*cm, ypos * cm, str(storno.rechnungsnr.kundennr.firma))
#         c.drawString(15*cm, ypos * cm, '{:.2f}'.format(storno.rechnungsnr.total /(1+storno.rechnungsnr.mwst) * storno.rechnungsnr.mwst))
#         c.drawString(17*cm, ypos * cm, '{:.2f}'.format(storno.rechnungsnr.total))
#
#         ypos += 0.5
#
#         c.line(2*cm, ypos * cm, 18.5*cm, ypos*cm)
#
#
#
#         c.setFont("Helvetica", 10)
#
#
#
#
#         c.save()
#
#         return '/static/files/stornos/ST_' + str(stornonr) + '.pdf'
#
#     def write_gutschrift(self, queryset):
#         # Creating Canvas
#         auftrag = queryset[0]
#         title = 'Gutschrift:'
#         gutschriftnr = str(auftrag.gutschriftnr.gutschriftenid)
#         filename = 'Gutschrift' + gutschriftnr + '.pdf'
#
#         c = canvas.Canvas(self.buffer, pagesize=pagesizes.A4, bottomup=0)
#         (width, height) = pagesizes.A4
#
#         c.translate(10, 40)
#
#         ## Logo
#         c.scale(1, -1)
#         c.drawImage(self.header_img_path, 3, -60, width=550, height=120)
#         # Title Section
#         # Again Inverting Scale For strings insertion
#         c.scale(1, -1)
#         # Again Setting the origin back to (0,0) of top-left
#         c.translate(-10, -40)
#
#
#
#
#
#
#         c.setFont("Helvetica", 11)
#
#         c.drawString(12*cm, 5*cm, str(auftrag.partnernr.firma))
#         c.drawString(12*cm, 5.5*cm, str(auftrag.partnernr.adresse))
#         c.drawString(12*cm, 6*cm, str(auftrag.partnernr.locationnr.plz))
#         c.drawString(13*cm, 6*cm, str(auftrag.partnernr.locationnr.ort))
#
#         c.setFont("Helvetica", 8)
#         c.drawString(2*cm, 5*cm, "Pfister Transporte AG")
#         c.drawString(2*cm, 5.5*cm, "Heimenhausenstrasse 4")
#         c.drawString(2*cm, 6*cm, "3377 Walliswil bei Wangen")
#         c.drawString(2*cm, 6.5*cm, "MWST-NR : 07AABCS1429B1Z")
#
#
#         c.drawString(2*cm, 9.5*cm, "Datum :")
#         c.drawString(4.5*cm, 9.5*cm, auftrag.gutschriftnr.date.strftime("%d.%m.%Y"))
#         c.drawString(2 * cm, 10 * cm, "Sachbearbeiter :")
#         c.drawString(4.5 * cm, 10 * cm, 'Hans Pfister')
#         c.drawString(2*cm, 10.5*cm, "Email :")
#         c.drawString(4.5  * cm, 10.5 * cm, "disp@pfister-transporte.ch")
#         c.drawString(2*cm, 11*cm, "Tel. :")
#         c.drawString(4.5  * cm, 11 * cm, "+41 32 631 21 88")
#
#
#
#
#         c.setFont("Helvetica-Bold", 11)
#         c.drawString(2*cm, 14 * cm, title)
#         c.drawString(5.5 * cm, 14 * cm, gutschriftnr)
#
#         c.setFont("Helvetica", 11)
#        # c.setLineWidth(0.25)
#         c.drawString(2*cm, 15 * cm, "Datum")
#         c.drawString(4*cm, 15 * cm, "Beschreibung")
#         c.drawString(10*cm, 15 * cm, "Einheit")
#         c.drawString(12*cm, 15 * cm, "Menge")
#         c.drawString(15*cm, 15 * cm, "Preis")
#         c.drawString(17*cm, 15 * cm, "Total")
#
#
#         c.line(2*cm, 15.5 * cm, 18.5*cm, 15.5*cm)
#
#         c.setFont("Helvetica", 10)
#
#         ypos = 16.5
#         sub_total = 0
#         for auftrag in queryset:
#             auftrags_total_excl_verm = auftrag.menge * auftrag.preis - auftrag.vermittlungsgebühr
#             c.drawString(2*cm, ypos * cm, str(auftrag.datefrom.strftime("%d.%m.%Y")))
#             if auftrag.referenz != None:
#                 c.drawString(4*cm, ypos * cm, str(auftrag.referenz) + ' '+ str(auftrag.beschreibung)[0:30])
#             else:
#                 c.drawString(4 * cm, ypos * cm, str(auftrag.beschreibung))
#             c.drawString(10*cm, ypos * cm, str(auftrag.einheitnr.einheit))
#             c.drawString(12*cm, ypos * cm, str(auftrag.menge))
#             c.drawString(15*cm, ypos * cm, str(auftrags_total_excl_verm / auftrag.menge))
#             c.drawString(17*cm, ypos * cm, str(auftrags_total_excl_verm))
#             sub_total += auftrags_total_excl_verm
#             ypos = self.addy(ypos, c, 0.5)
#
#         c.setFont("Helvetica", 10)
#
#         ypos = self.addy(ypos, c, 0.5)
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'Sub-Total')
#         c.drawString(15 * cm, ypos * cm, auftrag.currencynr.currency)
#         c.drawString(17 * cm, ypos * cm, str(sub_total))
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'MWST')
#         if auftrag.export_import == 1:
#             mwst = 0
#             c.drawString(12 * cm, ypos * cm, 'MWST (0.0%)')
#
#             c.drawString(15 * cm, ypos * cm, auftrag.currencynr.currency)
#             c.drawString(17 * cm, ypos * cm, '0.00')
#         else:
#             mwst = 0.077
#             c.drawString(12 * cm, ypos * cm, 'MWST (7.7%)')
#             c.drawString(15 * cm, ypos * cm, auftrag.currencynr.currency)
#             c.drawString(17 * cm, ypos * cm, str(sub_total / 100 * 7.7))
#
#         ypos = self.addy(ypos, c, 0.5)
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos = self.addy(ypos, c, 0.5)
#         c.drawString(12 * cm, ypos * cm, 'Total')
#         c.drawString(15 * cm, ypos * cm, auftrag.currencynr.currency)
#         total = round(2*(sub_total * (1+mwst)), 1)
#         total = total / 2
#         c.drawString(17 * cm, ypos * cm, str(total))
#         ypos += 0.5
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#         ypos += 0.1
#         c.line(12 * cm, ypos * cm, 18.5 * cm, ypos * cm)
#
#
#         c.save()
#         self.buffer.seek(0)
#
#         filename = os.path.join(BASE_DIR, 'files', 'gutschriften', 'ST_' + str(gutschriftnr) + '.pdf')
#         with open(filename, 'wb') as file:
#             file.write(self.buffer.read())
#         return (self.buffer, total, mwst)
#
#     def addy(self, ypos, canvas, amount):
#         ypos += amount
#         if ypos >=26:
#             self.page_counter += 1
#             page_num = canvas.getPageNumber()
#             canvas.drawString(18 * cm, 29* cm, 'Seite: ' + str(page_num))
#             canvas.showPage()
#             ypos = 3
#             canvas.setFont("Helvetica", 10)
#         return ypos
#
#     def generate_qr_bill(self, rechnungsnr, customer_name, customer_plz, cusotmer_city, customer_country, amount, account, language):
#
#         debtor = {'name' :str(customer_name),'pcode' : str(customer_plz), 'city':str(cusotmer_city), 'country':str(customer_country)}
#         my_bill = QRBill(
#             account= account,
#             creditor={
#                 'name': 'Pfister Transporte AG', 'pcode': '3380', 'city': 'Wangen an der Aare', 'country': 'CH'},
#             amount= str(amount),
#             language=language,
#             debtor= debtor)
#
#         with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
#             my_bill.as_svg(temp)
#             temp.seek(0)
#             drawing = svg2rlg(temp)
#
#             filename = os.path.join(BASE_DIR,'static','files', 'qrbills', str(rechnungsnr)+ '.pdf')
#             renderPDF.drawToFile(drawing, filename)
#
#             pages = convert_from_path(filename)
#             jpeg_file_name = os.path.join(BASE_DIR,'static','files', 'qrbills' ,str(rechnungsnr) +'.jpg')
#             pages[0].save(jpeg_file_name, 'JPEG')
#
#             return jpeg_file_name
#
#
#         return jpeg_file_name
#
#     def queryset_to_excel(self, queryset):
#         # response = HttpResponse(
#         #     content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#         # )
#         # response['Content-Disposition'] = 'attachment; filename={date}-export.xlsx'.format(
#         #     date=dt.datetime.now().strftime('%Y-%m-%d'),
#         # )
#
#         filename = os.path.join(BASE_DIR, 'static', 'files', 'export.xlsx')
#         workbook = Workbook()
#         worksheet = workbook.active
#
#         columns = list(queryset[0].keys())
#
#         for colnr, column in enumerate(columns, 1):
#             cell = worksheet.cell(row=1, column=colnr)
#             cell.value = column
#
#
#
#         for rownr, row in enumerate(queryset,2):
#             for colnr, column in enumerate(row.values(),1):
#                 cell = worksheet.cell(row=rownr, column=colnr)
#                 cell.value = column
#
#
#
#
#         # #
#         workbook.save(filename)
#         # #
#         return '/static/files/export.xlsx'
#
#
#     def queryset_to_csv(self, queryset):
#         filename = os.path.join(BASE_DIR, 'static', 'files', 'export.csv')
#         columns = list(queryset[0].keys())
#         with open(filename, 'w') as csvfile:
#             # creating a csv dict writer object
#             writer = csv.DictWriter(csvfile, fieldnames=columns)
#
#             # writing headers (field names)
#             writer.writeheader()
#
#             # writing data rows
#             for data in queryset:
#                 writer.writerow(data)
#
#
#
#
#         return '/static/files/export.csv'
#
#     def draw_einteilung(self,fzmapping, scheduled_tasks, scheduledate, fremdfahrer):
#         c = canvas.Canvas(self.buffer,pagesize=pagesizes.landscape(pagesizes.A4), bottomup=0)
#         width, height = pagesizes.A4
#         c.setFillColor(colors.black)
#
#         c.setFont("Helvetica-Bold", 12)
#         c.drawString(1 * cm, 1 * cm, "Einteilung vom " + scheduledate.strftime('%d.%m.%Y'))
#
#         c.setFont("Helvetica", 7)
#
#
#
#         c.drawString(1 * cm, 2 * cm, "Fahrzeug")
#         c.drawString(3 * cm, 2 * cm, "Mitarbeiter")
#         xpos = 5
#         c.setFont("Helvetica", 7)
#
#         max_y = len(fzmapping) + len(fremdfahrer)
#
#         ypos = 2.25
#         xpos = 1
#
#         for i in range(max_y):
#             c.setLineWidth(0)
#             if i % 2:
#                 c.setFillColor(colors.whitesmoke)
#                 c.setStrokeColor(colors.white)
#                 c.rect(5 * cm, ypos * cm, 24 * cm, 1 * cm, fill=1)
#             ypos += 1
#
#         ypos = 2.1
#         xpos = 5
#
#
#         for i in range(25):
#             c.setFillColor(colors.black)
#             c.drawCentredString(xpos * cm, 2 * cm, str(i) + ':00')
#             c.setLineWidth(0.5)
#             c.setStrokeColor(colors.gray)
#             c.line(xpos * cm, 2.1 * cm, xpos * cm, (max_y+2.25) * cm)
#             c.setLineWidth(0.01)
#             if i < 24:
#                 c.setStrokeColor(colors.lightgrey)
#                 c.line((xpos + 0.25) * cm, 2.25 * cm, (xpos + 0.25) * cm, (max_y+2.25) * cm)
#                 c.line((xpos + 0.5) * cm, 2.25 * cm, (xpos + 0.5) * cm, (max_y+2.25) * cm)
#                 c.line((xpos + 0.75) * cm, 2.25 * cm, (xpos + 0.75) * cm, (max_y+2.25) * cm)
#             xpos += 1
#
#         ypos = 2.25
#         xpos = 1
#         c.line(1 * cm, ypos * cm, 29 * cm, ypos * cm)
#
#         for fz in fzmapping:
#             print(fz)
#             ypos += 0.5
#             c.setFillColor(colors.black)
#             c.drawString(xpos*cm, ypos*cm, str(fz['Nummernschild']))
#             if fz['Name'] or fz['Vorname']:
#                 c.drawString(3 * cm, ypos * cm, str(fz['Name']) +' '+ str(fz['Vorname']))
#             else:
#                 c.drawString(3 * cm, ypos * cm, 'Nicht zugewiesen')
#
#             ypos += 0.5
#             c.line(1 * cm, ypos * cm, 5 * cm, ypos * cm)
#             ypos -= 1
#             for i in scheduled_tasks:
#
#                 if i.fahrzeugnr != None and fz['FahrzeugID'] == i.fahrzeugnr.fahrzeugid:
#
#                     datetimefrom = dt.datetime.combine(i.datefrom, i.timefrom)
#                     datetimeto = dt.datetime.combine(i.dateto, i.timeto)
#                     seconds_from= (datetimefrom-scheduledate).seconds
#                     seconds_to = (datetimeto-scheduledate).seconds
#                     rel_pos_from = seconds_from / 86400
#                     rel_pos_to = seconds_to / 86400
#                     abs_pos_from = 5 +(24*rel_pos_from)
#                     width = (rel_pos_to - rel_pos_from) * 24
#
#                     if (datetimeto - scheduledate).days >= 1 and (scheduledate - datetimefrom).days >= 1:
#                         abs_pos_from = 5
#                         width = 24
#
#                     elif (scheduledate-datetimefrom).days >= 1 and (datetimeto-scheduledate).days <1:
#                         abs_pos_from = 5
#                         width = (rel_pos_to) * 24
#                     elif (datetimeto-scheduledate).days >= 1 and  (scheduledate - datetimefrom).days < 1:
#                         width = (1-rel_pos_from) * 24
#                     else:
#                         abs_pos_from = 5 + (24 * rel_pos_from)
#                         width = (rel_pos_to - rel_pos_from) * 24
#                     string_start_pos = abs_pos_from + 0.5 * width
#
#                     c.setFillColor(colors.indianred)
#                     c.rect(abs_pos_from*cm, ypos *cm, width*cm, 1*cm, fill=1)
#                     c.setFillColor(colors.white)
#                     ypos += 0.5
#                     c.drawCentredString(string_start_pos * cm, ypos * cm, str(i.beschreibung))
#                     ypos += 0.25
#                     c.drawCentredString(string_start_pos * cm, ypos * cm, str(i.aufliegernr))
#                     ypos -= 0.75
#                     #ypos -= 0.5
#             ypos += 1
#         for index, fahrer in enumerate(fremdfahrer):
#
#             ypos += 0.5
#             c.setFillColor(colors.black)
#             c.drawString(xpos * cm, ypos * cm, fahrer.firma)
#             #c.drawString(3 * cm, ypos * cm, str(fz[3]) + str(fz[4]))
#             ypos += 0.5
#             if index == (len(fremdfahrer) -1):
#                 c.line(1 * cm, ypos * cm, 29 * cm, ypos * cm)
#             else:
#                 c.line(1 * cm, ypos * cm, 5 * cm, ypos * cm)
#             ypos -= 1
#             for i in scheduled_tasks:
#
#                 if i.partnernr != None and fahrer.fremdfahrerid == i.partnernr.fremdfahrerid:
#                     datetimefrom = dt.datetime.combine(i.datefrom, i.timefrom)
#                     datetimeto = dt.datetime.combine(i.dateto, i.timeto)
#                     seconds_from = (datetimefrom - scheduledate).seconds
#                     seconds_to = (datetimeto - scheduledate).seconds
#                     rel_pos_from = seconds_from / 86400
#                     rel_pos_to = seconds_to / 86400
#                     abs_pos_from = 5 + (24 * rel_pos_from)
#                     width = (rel_pos_to - rel_pos_from) * 24
#                     if (datetimeto - scheduledate).days >= 1 and (scheduledate - datetimefrom).days >= 1:
#                         abs_pos_from = 5
#                         width = 24
#
#                     elif (scheduledate - datetimefrom).days >= 1 and (datetimeto - scheduledate).days < 1:
#                         abs_pos_from = 5
#                         width = (rel_pos_to) * 24
#                     elif (datetimeto - scheduledate).days >= 1 and (scheduledate - datetimefrom).days < 1:
#                         width = (1 - rel_pos_from) * 24
#                     else:
#                         abs_pos_from = 5 + (24 * rel_pos_from)
#                         width = (rel_pos_to - rel_pos_from) * 24
#                     string_start_pos = abs_pos_from + 0.5 * width
#
#                     c.setFillColor(colors.indianred)
#                     c.rect(abs_pos_from * cm, ypos * cm, width * cm, 1 * cm, fill=1)
#                     c.setFillColor(colors.white)
#                     ypos += 0.5
#                     c.drawCentredString(string_start_pos * cm, ypos * cm, str(i.beschreibung))
#                     ypos += 0.25
#                     c.drawCentredString(string_start_pos * cm, ypos * cm, str(i.aufliegernr))
#                     ypos -= 0.75
#                         # ypos -= 0.5
#
#             ypos += 1
#
#
#
#         c.save()
#         self.buffer.seek(0)
#         return self.buffer
#
#
#
# if __name__ == '__main__':
#     docwriter = DocumentWriter()
#     docwriter.draw_einteilung()
#






