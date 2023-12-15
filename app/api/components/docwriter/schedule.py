import os

from reportlab.lib import pagesizes, colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import datetime as dt
import dateutil.parser
from api.components import Document


class SchedulePDF(Document):
    def __init__(self, date, language:str, output_path:str):
        self.page_size = landscape(pagesizes.A4)
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




    def header(self):
        '''draw the header of the scheduler document'''
        self.setFillColor(colors.black)

        self.setFont("Helvetica-Bold", 12)
        self.c.drawString(1 * cm, 1 * cm, f'{self.labels["title"][self.language]}: {self.date}')

        self.setFont("Helvetica", 7)

        self.c.drawString(1 * cm, 2 * cm, f'{self.labels["employee_label"][self.language]}')
        self.c.drawString(3 * cm, 2 * cm, f'{self.labels["asset_label"][self.language]}')


        self.y = 2.1
        self.x = 5

        for i in range(25):
            self.setFillColor(colors.black)
            self.setLineWidth(0.2)
            self.c.drawCentredString(self.x * cm, 2 * cm, str(i) + ':00')
            self.setLineWidth(0.2)
            self.setStrokeColor(colors.black)
            self.x += 1

        self.y = 2.25
        self.x = 1

        self.c.line(1 * cm, self.y * cm, 29 * cm, self.y * cm)


    def draw_second_page_header(self):
        self.header()


    def draw_task(self,task_id, task_description, asset_1, asset_2, ts_from, ts_to):
        ''' draw single task into lane of the schedule'''


        task_resources = asset_1 + ' ' + asset_2

        self.c.drawCentredString(3.5 * cm, self.y * cm, task_resources)

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
        self.setFillColor(customColor)
        self.c.rect(offset_left * cm, (self.y - 0.4) * cm, width * cm, 0.8 * cm, fill=1)
        self.setFillColor(colors.white)

        string_pos = (width / 2) + offset_left
        self.c.drawCentredString(string_pos * cm, self.y * cm, f'{task_id} - {task_description}')






    def draw(self):


        self.header()

        self.increase_y(0.5)

        for index, employee in enumerate(self.employees):
            self.setFillColor(colors.black)
            self.x = 1
            self.c.drawString(self.x * cm, self.y * cm, employee['name'])

            subset = self.filter_data(employee['id'])

            max_y = len(subset)+ self.y -0.5
            self.x = 5
            self.increase_y(-0.5)

            for i in range(25):
                self.setLineWidth(0.5)
                self.setStrokeColor(colors.gray)
                self.c.line(self.x * cm, self.y * cm, self.x * cm, (max_y) * cm)
                self.setLineWidth(0.01)
                if i < 24:
                    self.setStrokeColor(colors.lightgrey)
                    self.c.line((self.x + 0.25) * cm, self.y * cm, (self.x + 0.25) * cm, (max_y) * cm)
                    self.c.line((self.x + 0.5) * cm, self.y * cm, (self.x + 0.5) * cm, (max_y) * cm)
                    self.c.line((self.x + 0.75) * cm, self.y * cm, (self.x + 0.75) * cm, (max_y) * cm)
                self.x += 1

            self.increase_y(0.5)

            for task_index , task in enumerate(subset):
                if len(task['description'].replace('\n', ' ')) > 25:
                    task_description = task['description'].replace('\n', ' ')[:20] + '...'
                else:
                    task_description = task['description'].replace('\n', ' ')

                self.draw_task(task['id'], task_description, task['asset_1'], task['asset_2'], task['ts_from'], task['ts_to'])


                self.setLineWidth(0.2)
                #self.increase_y(0.5)
                if len(subset) > 1 and task_index != len(subset)-1:
                    self.c.line(5 * cm, self.y * cm, 29 * cm, self.y * cm)
                self.increase_y(0.5)

            #self.increase_y(0.5)
            self.setLineWidth(0.2)
            self.setStrokeColor(colors.black)
            self.c.line(1 * cm, self.y * cm, 29 * cm, self.y * cm)
            self.increase_y(0.5)







        self.c.save()







