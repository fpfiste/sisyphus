
from .document import Document
from reportlab.lib.units import cm

class DeliveryNote(Document):
    def __init__(self, language:str, output_path:str):
        super().__init__(language, 'DeliveryNote', output_path=output_path)
        self.position = None


    def add_position(self, position_id,date,  time, description, unit, amount, reference):
        task = {
            'position_id': position_id,
            'date': date if date != None else '',
            'time':time if time != None else '',
            'description': description if description != None else '',
            'unit' : unit if unit != None else '',
            'amount' : amount if amount != None else '',
            'reference' : reference if reference != None else ''
        }

        self.document_id = position_id
        self.position = task


    def draw(self):

        c = self.draw_template()


        c.drawString(2 * cm, 8.5 * cm, f"Sachbearbeiter: {self.company['agent']}")
        c.drawString(2 * cm, 9 * cm, f"Email: {self.company['email']}")
        c.drawString(2 * cm, 9.5 * cm, f"Tel.: {self.company['phone']}")

        c.drawString(2 * cm, 11 * cm, f"Kunden-Nr.: {self.customer['id']}")

        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont



        c.setFont("Helvetica-Bold", 14)
        c.drawString(2 * cm, 14.5 * cm, f'Lieferschein: {self.document_id}')

        c.setFont("Helvetica-Bold", 10)
        # c.setLineWidth(0.25)
        c.drawString(2 * cm, 16 * cm, "Datum")
        c.drawString(5 * cm, 16 * cm, "Beschreibung")
        c.drawRightString(16.5 * cm, 16 * cm, "Einheit")
        c.drawRightString(19 * cm, 16 * cm, "Menge")

        c.setLineWidth(0.2)
        c.setFont("Helvetica", 10)
        c.line(2 * cm, 16.3 * cm, 19 * cm, 16.3 * cm)


        ypos = 17

        c.setFont("Helvetica", 10)
        c.drawString(2 * cm, ypos * cm, str(self.position['date']))

        c.setFont("Helvetica-Bold", 10)
        c.drawString(5 * cm, ypos * cm, f'Auftrag: {self.position["position_id"] }')
        ypos = self.addy(ypos, c, 0.5)
        c.setFont("Helvetica", 8)
        c.drawString(5 * cm, ypos * cm, f'Beschreibung: {self.position["description"]}')
        ypos = self.addy(ypos, c, 0.5)

        if self.position['reference'] not in (None, ''):
            c.drawString(5 * cm, ypos * cm, f'Referenz: {self.position["reference"]}')
            ypos = self.addy(ypos, c, 0.5)


        c.drawString(5 * cm, ypos * cm, f'Zeit: {self.position["time"]}')
        ypos = self.addy(ypos, c, -2)

        ypos = 17
        c.setFont("Helvetica", 10)
        c.drawRightString(16.5 * cm, ypos * cm, self.position['unit'])
        c.drawRightString(19 * cm, ypos * cm, "%.2f" % self.position["amount"])


        ypos = self.addy(ypos, c, 3)

        c.setFont("Helvetica", 10)

        c.line(2 * cm, ypos * cm, 19 * cm, ypos * cm)

        # Title Section
        # Again Inverting Scale For strings insertion
        page_num = c.getPageNumber()
        c.drawString(18 * cm, 29 * cm, 'Seite: ' + str(page_num))

        c.drawString(12 * cm, 22 * cm, 'Unterschrift Warenempfänger **')
        c.rect(12 * cm, 22.5 * cm, 5 * cm, 3 * cm, fill=0)

        c.setFont("Helvetica", 6)
        c.drawString(2 * cm, 28 * cm,
                     '** Mit Ihrer Unterschrift bestätigen Sie den kompletten Erhalt der Ware gemäss Vereinbarung. Zudem besätigen Sie dass die Ware ohne jegliche Mängel überliefert wurde.')
        c.showPage()

        c.save()

        return


if __name__ == '__main__':

    #doc = Invoice(1,  '2023-09-15', 0.077, 30, 'CHF', '', language='de')
    doc = DeliveryNote('de')

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