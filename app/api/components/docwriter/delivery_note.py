import decimal
import datetime as dt
import textwrap

from reportlab.lib import colors, pagesizes

from .document import Document
from reportlab.lib.units import cm

class DeliveryNote(Document):
    def __init__(self, language:str, output_path:str):
        self.page_size = pagesizes.A4
        super().__init__(language, 'DeliveryNote', output_path=output_path)
        self.position = None
        self.doc_date = dt.date.today()


    def add_position(self, position_id,date,  time, description, internal_info, unit, amount, reference, employee_1, employee_2, asset_1, asset_2):
        task = {
            'position_id': position_id,
            'date': date if date != None else '',
            'time':time if time != None else '',
            'description': description if description != None else '',
            'internal_info' : internal_info if internal_info != None else '',
            'unit' : unit if unit != None else '',
            'amount' : amount if amount != None else '',
            'reference' : reference if reference != None else '',
            'employee_1':  employee_1 if employee_1 != None else '',
            'employee_2':employee_2 if employee_2 != None else '',
            'asset_1': asset_1 if asset_1 != None else '',
            'asset_2': asset_2 if asset_2 != None else ''
        }

        self.document_id = position_id
        self.position = task


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



    def draw_table_row(self, key, value, last_line=False):

        y_start = self.y
        self.setFont("Helvetica", 10)
        self.setStrokeColor(colors.lightgrey)
        self.setLineWidth(0.2)
        self.c.line(1.5 * cm, self.y * cm, 19.5 * cm, self.y * cm)

        self.increase_y(0.5)

        self.c.drawString(self.x * cm, self.y * cm, f"{key}:")

        wrapper = textwrap.TextWrapper(width=50)

        for line in str(value).split('\n'):
            sublines = wrapper.wrap(text=line)
            for line in sublines:
                self.c.drawString(7 * cm, self.y * cm, f'{line}')
                self.increase_y(0.5)

        if last_line:
            self.c.line(1.5 * cm, self.y * cm, 19.5 * cm, self.y * cm)

        if y_start > self.y:
            y_start = 1
        self.c.line(1.5 * cm, y_start * cm, 1.5 * cm, self.y * cm)
        self.c.line(5 * cm, y_start * cm, 5 * cm, self.y * cm)
        self.c.line(19.5* cm, y_start * cm, 19.5 * cm, self.y * cm)


    def draw(self):
        self.header()

        self.setFont("Helvetica-Bold", 14)
        self.c.drawString(2 * cm, 14.5 * cm, f'Auftrag: {self.document_id}')
        self.setFont("Helvetica", 10)

        self.c.setStrokeColor(colors.lightgrey)
        self.setLineWidth(0.2)

        self.y = 15.5


        self.draw_table_row('Beschreibung', self.position['description'])
        self.draw_table_row('Interne Info', self.position['internal_info'])
        self.draw_table_row('Start', f"{self.position['date']} {self.position['time']}")
        self.draw_table_row('Mitarbeiter', f"{self.position['employee_1']} | {self.position['employee_2']}")
        self.draw_table_row('Assets', f"{self.position['asset_1']} | {self.position['asset_2']}")
        self.draw_table_row('Einheit', f"{self.position['unit']}")
        self.draw_table_row('Menge', f"{self.position['amount']}", last_line=True)



        self.c.save()
        return self.c


