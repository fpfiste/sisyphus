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
        self.assets = []
        self.tasks = []
        self.language = language
        self.labels = {
            'title': {'en': 'Schedule Date', 'ch': 'Kalender vom'},
            'employee_label': {'en': 'Employees', 'ch': 'Mitarbeiter'},
            'asset_label': {'en': 'Assets', 'ch': 'Ressourcen'},

        }

    def add_employee(self, id, name):
        ids = [i['id'] for i in self.employees]

        if id not in ids:
            self.employees.append({
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
    def add_task(self,id, description, date_from, time_from, date_to, time_to, employee_1, employee_2, asset_1='', asset_2=''):
        self.tasks.append({
            'id':id,
            'description':description,
            'ts_from' : dt.datetime.combine(date_from, time_from),
            'ts_to' : dt.datetime.combine(date_to, time_to),
            'employee_1': employee_1,
            'employee_2': employee_2,
            'asset_1' : '' if asset_1 == None else asset_1,
            'asset_2' : '' if asset_2 == None else asset_2,
        })




    def filter_data(self, id_employee):
        subset = [i for i in self.tasks if i['employee_1'] == id_employee or i['employee_2'] == id_employee]
        return subset




    def header(self, c):
        '''draw the header of the scheduler document'''
        c.setFillColor(colors.black)

        c.setFont("Helvetica-Bold", 12)
        c.drawString(1 * cm, 1 * cm, f'{self.labels["title"][self.language]}: {self.date}')

        c.setFont("Helvetica", 7)

        c.drawString(1 * cm, 2 * cm, f'{self.labels["employee_label"][self.language]}')
        c.drawString(3 * cm, 2 * cm, f'{self.labels["asset_label"][self.language]}')


        ypos = 2.1
        xpos = 5


        for i in range(25):
            c.setFillColor(colors.black)
            c.setLineWidth(0.2)
            c.drawCentredString(xpos * cm, 2 * cm, str(i) + ':00')
            c.setLineWidth(0.2)
            c.setStrokeColor(colors.black)
            xpos += 1

        ypos = 2.25
        xpos = 1

        c.line(1 * cm, ypos * cm, 29 * cm, ypos * cm)

        return c , xpos, ypos


    def draw_task(self, c, ypos, task_id, task_description, asset_1, asset_2, ts_from, ts_to):
        ''' draw single task into lane of the schedule'''


        task_resources = asset_1 + ' ' + asset_2

        c.drawCentredString(3.5 * cm, ypos * cm, task_resources)

        seconds_from = (ts_from - self.date).seconds
        seconds_to = (ts_to - self.date).seconds

        if (ts_from - self.date).days < 0:
            seconds_from = 0

        if (ts_to - self.date).days >= 1:
            seconds_to = 86400

        duration = 86400 - seconds_from - (86400 - seconds_to)
        offset_left = (seconds_from / 86400 * 24) + 5

        width = (duration / 86400 * 24)

        customColor = colors.Color(red=(88.0 / 255), green=(129.0 / 255), blue=(87.0 / 255))
        c.setFillColor(customColor)
        c.rect(offset_left * cm, (ypos - 0.5) * cm, width * cm, 1 * cm, fill=1)
        c.setFillColor(colors.white)

        string_pos = (width / 2) + offset_left
        c.drawCentredString(string_pos * cm, ypos * cm, f'{task_id} - {task_description}')

        return c

    def set_settings(self, c):
        c.setFillColor(colors.black)



    def draw(self):
        file_name = os.path.join(self.file_name)
        c = canvas.Canvas(file_name, pagesize=pagesizes.landscape(pagesizes.A4), bottomup=0)

        c, xpos, ypos = self.header(c)

        ypos = self.addy(ypos, c, 0.5)

        for index, employee in enumerate(self.employees):

            xpos = 1
            c.drawString(xpos * cm, ypos * cm, employee['name'])

            subset = self.filter_data(employee['id'])

            max_y = len(subset)+ ypos -0.5
            xpos = 5
            ypos = self.addy(ypos, c, -0.5)

            for i in range(25):
                c.setLineWidth(0.5)
                c.setStrokeColor(colors.gray)
                c.line(xpos * cm, ypos * cm, xpos * cm, (max_y) * cm)
                c.setLineWidth(0.01)
                if i < 24:
                    c.setStrokeColor(colors.lightgrey)
                    c.line((xpos + 0.25) * cm, ypos * cm, (xpos + 0.25) * cm, (max_y) * cm)
                    c.line((xpos + 0.5) * cm, ypos * cm, (xpos + 0.5) * cm, (max_y) * cm)
                    c.line((xpos + 0.75) * cm, ypos * cm, (xpos + 0.75) * cm, (max_y) * cm)
                xpos += 1

            ypos = self.addy(ypos, c, 0.5)

            for task_index , task in enumerate(subset):
                print(task['description'].replace('\n', ' '))
                if len(task['description'].replace('\n', ' ')) > 25:
                    task_description = task['description'].replace('\n', ' ')[:20] + '...'
                else:
                    task_description = task['description'].replace('\n', ' ')

                self.draw_task(c, ypos, task['id'], task_description, task['asset_1'], task['asset_2'], task['ts_from'], task['ts_to'])


                c.setLineWidth(0.2)
                ypos = self.addy(ypos, c, 0.5)
                if len(subset) > 1 and task_index != len(subset)-1:
                    c.line(5 * cm, ypos * cm, 29 * cm, ypos * cm)
                ypos = self.addy(ypos, c, 0.5)

            ypos = self.addy(ypos, c, -0.5)
            c.setLineWidth(0.2)
            c.setStrokeColor(colors.black)
            c.line(1 * cm, ypos * cm, 29 * cm, ypos * cm)
            ypos = self.addy(ypos, c, 0.5)







        c.save()







