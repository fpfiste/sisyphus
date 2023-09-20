import os

from reportlab.lib import pagesizes, colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import datetime as dt
import dateutil.parser
from api.components import Document


class SchedulePDF(Document):
    def __init__(self, date, language:str, output_path:str):
        super().__init__(language, 'Schedule', output_path=output_path)
        self.date = dateutil.parser.parse(date)
        self.employees = []
        self.subcontractors = []
        self.assets = []
        self.tasks = []
        self.language = language
        self.labels = {
            'title': {'en': 'Schedule Date', 'ch': 'Kalender vom'},
            'employee_label': {'en': 'Employees', 'ch': 'Mitarbeiter'},
            'asset_label': {'en': 'Assets', 'ch': 'Ressourcen'},
            'subcon_label': {'en': 'Subcontractors', 'ch': 'Subunternehmer'}

        }

    def add_employee(self, id, name):
        ids = [i['id'] for i in self.employees]

        if id not in ids:
            self.employees.append({
                'id' : id,
                'name' : name
            })

    def add_subcontractor(self, id, name):
        ids = [i['id'] for i in self.subcontractors]

        if id not in ids:
            self.subcontractors.append({
            'id' : id,
            'name' : name
        })

    def add_asset(self, id, name):
        ids = [i['id'] for i in self.assets]

        if id not in ids:
            self.assets.append({
            'id' : id,
            'name': name
        })
    def add_task(self,id, description, date_from, time_from, date_to, time_to, employee_1, employee_2, asset_1, asset_2, subcontractor):
        self.tasks.append({
            'id':id,
            'description':description,
            'ts_from' : dt.datetime.combine(date_from, time_from),
            'ts_to' : dt.datetime.combine(date_to, time_to),
            'employee_1': employee_1,
            'employee_2': employee_2,
            'asset_1' : asset_1,
            'asset_2' : asset_2,
            'subcontractor' : subcontractor
        })


    def filter_data(self, id_employee):
        subset = [i for i in self.tasks if i['employee_1'] == id_employee or i['employee_2'] == id_employee]
        return subset


    def draw(self):
        file_name = os.path.join(self.file_name)
        c = canvas.Canvas(file_name, pagesize=pagesizes.landscape(pagesizes.A4), bottomup=0)
        width, height = pagesizes.A4
        c.setFillColor(colors.black)

        c.setFont("Helvetica-Bold", 12)
        c.drawString(1 * cm, 1 * cm, f'{self.labels["title"][self.language]}: {self.date}')

        c.setFont("Helvetica", 7)

        c.drawString(1 * cm, 2 * cm, f'{self.labels["employee_label"][self.language]}')
        c.drawString(3 * cm, 2 * cm, f'{self.labels["asset_label"][self.language]}')

        ypos = 2.25
        xpos = 1

        max_y = len(self.employees) + len(self.subcontractors)
        for i in range(max_y):
            c.setLineWidth(0)
            if i % 2:
                c.setFillColor(colors.whitesmoke)
                c.setStrokeColor(colors.white)
                c.rect(5 * cm, ypos * cm, 24 * cm, 1 * cm, fill=1)
            ypos += 1

        c.setLineWidth(0.5)
        c.setStrokeColor(colors.gray)
        c.setFillColor(colors.black)
        c.line(xpos * cm, 2.1 * cm, xpos * cm, (max_y + 2.25) * cm)
        ypos = 2.1
        xpos = 5

        for i in range(25):
            c.setFillColor(colors.black)
            c.drawCentredString(xpos * cm, 2 * cm, str(i) + ':00')
            c.setLineWidth(0.5)
            c.setStrokeColor(colors.gray)
            c.line(xpos * cm, 2.1 * cm, xpos * cm, (max_y+2.25) * cm)
            c.setLineWidth(0.01)
            if i < 24:
                c.setStrokeColor(colors.lightgrey)
                c.line((xpos + 0.25) * cm, 2.25 * cm, (xpos + 0.25) * cm, (max_y+2.25) * cm)
                c.line((xpos + 0.5) * cm, 2.25 * cm, (xpos + 0.5) * cm, (max_y+2.25) * cm)
                c.line((xpos + 0.75) * cm, 2.25 * cm, (xpos + 0.75) * cm, (max_y+2.25) * cm)
            xpos += 1

        ypos = 2.25
        xpos = 1
        c.line(1 * cm, ypos * cm, 29 * cm, ypos * cm)

        ypos += 0.5
        for employee in self.employees:
            c.setFillColor(colors.black)
            c.drawString(xpos * cm, ypos * cm, employee['name'])


            subset = self.filter_data(employee['id'])

            for task in subset:

                seconds_from = (task['ts_from'] - self.date).seconds
                duration = (task['ts_to'] - task['ts_from']).seconds

                if (task['ts_from'] - self.date).days > 0:
                    seconds_from = 0

                if (task['ts_to'] - task['ts_from']).days >= 1:
                    duration = 86400 - seconds_from

                x_offset = (seconds_from / 86400 * 24) + 5
                width = (duration / 86400 * 24)

                print((task['ts_to'] - self.date).days)
                print(x_offset)
                print(width)


                c.setFillColor(colors.indianred)
                c.rect(x_offset * cm, (ypos-0.5) * cm, width * cm, 1 * cm, fill=1)
                c.setFillColor(colors.white)

                string_pos = (width / 2 ) + x_offset
                c.drawCentredString(string_pos * cm, ypos * cm, f'{task["id"]} - {task["description"]}')


            ypos += 1

        ypos -= 0.5
        c.line(1 * cm, ypos * cm, 29 * cm, ypos * cm)
        c.save()