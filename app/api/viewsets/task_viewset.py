from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
import datetime as dt

from rest_framework.response import Response

from api.components import Tasks, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Tasks.objects.all()

        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])

        data = queryset.filter(**params)


        return data



    @action(detail=False, methods=['GET'])
    def listday(self, request):

        date = request.session.get('schedule_date')

        if date == None:
            date =  dt.date.today()
            request.session['schedule_date'] = date.strftime("%Y-%m-%d")
        tasks = Tasks.objects.filter(
                Q(task_date_from=date) |
                Q(task_date_to=date) |
                Q(task_date_from__lt= date, task_date_to__gt= date)


        )

        tasks = tasks.filter(fk_employee_1__isnull = False, task_time_from__isnull=False, task_time_to__isnull=False).order_by('task_date_from', 'task_time_from')

        print(tasks)
        print(request.session)


        serializer = self.get_serializer(tasks, many=True)


        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def getDate(self, request):
        date = request.session["schedule_date"]
        if date == None:
            date = dt.date.today()
            request.session['schedule_date'] = date.strftime("%Y-%m-%d")
        print(date)
        return Response({"date": request.session["schedule_date"]})



    @action(detail=False, methods=['POST'])
    def setDate(self, request):

        date = request.data.get('date')
        print(date)
        if date != None:
            request.session["schedule_date"] = date

        print(request.session['schedule_date'])
        return Response({"date" : request.session["schedule_date"]})

    @action(detail=False, methods=['GET'])
    def getOpenTasks(self, request):

        tasks = Tasks.objects.filter(
            Q(task_date_from__isnull=True) |
            Q(task_date_to__isnull=True) |
            Q(fk_employee_1__isnull=True)

        )

        print(len(tasks))
        print(request.session)

        serializer = self.get_serializer(tasks, many=True)

        return Response(serializer.data)