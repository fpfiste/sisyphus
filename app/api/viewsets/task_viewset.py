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

        data = queryset.filter(**params).order_by('-id_task')


        return data

    def create(self, request):
        print(request.data)
        request.data._mutable = True
        request.data['fk_task_state'] = "1"


        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        print(serializer.errors)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)




    def update(self, request,pk):

        request.data._mutable = True

        data = request.data.dict()
        date_from = request.data.get('task_date_from')
        date_to = request.data.get('task_date_to')
        time_from = request.data.get('task_time_from')
        time_to = request.data.get('task_time_to')
        employee = request.data.get('fk_employee_1')
        status = request.data.get('fk_task_state')


        if int(status) < 4:
            if (date_from != '') and (date_to != '') and (time_from != '') and (time_to != '') and (employee != ''):
                request.data['fk_task_state'] = "2"

                end_ts = dt.datetime.strptime(date_to + ' ' + time_to, '%Y-%m-%d %H:%M:%S')
                current_ts = dt.datetime.now()

                if end_ts < current_ts:
                    request.data['fk_task_state'] = "3"
            else:
                request.data['fk_task_state'] = "1"

        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data)

        serializer.is_valid()

        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, pk):
        request.data._mutable = True


        request.data['fk_task_state'] = "-1"
        instance = self.get_object()
        print(instance.__dict__)
        if instance.fk_task_state_id >= 4:
            return Response({'message': 'Task already billed'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data)

        serializer.is_valid()

        self.perform_update(serializer)
        print(request.data)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def listday(self, request):

        date = request.query_params.get('date')
        print(request.query_params)
        if date == None:
            date =  dt.date.today().strftime("%Y-%m-%d")

        tasks = Tasks.objects.filter(
                Q(task_date_from=date) |
                Q(task_date_to=date) |
                Q(task_date_from__lt= date, task_date_to__gt= date)


        )

        tasks = tasks.filter(fk_employee_1__isnull = False, task_time_from__isnull=False, task_time_to__isnull=False).order_by('task_date_from', 'task_time_from')

        serializer = self.get_serializer(tasks, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def getDate(self, request):
        date = request.session["schedule_date"]

        if date == None:
            date = dt.date.today()
            request.session['schedule_date'] = date.strftime("%Y-%m-%d")
        return Response({"date": request.session["schedule_date"]})



    @action(detail=False, methods=['POST'])
    def setDate(self, request):

        date = request.data.get('date')

        if date != None:
            request.session["schedule_date"] = date

        print(date)
        return Response({"date" : request.session["schedule_date"]})

    @action(detail=False, methods=['GET'])
    def getOpenTasks(self, request):

        tasks = Tasks.objects.filter(
            Q(task_date_from__isnull=True) |
            Q(task_date_to__isnull=True) |
            Q(fk_employee_1__isnull=True)
        ).order_by('id_task')
        print(tasks)
        tasks = tasks.filter(fk_task_state__gt=0)

        serializer = self.get_serializer(tasks, many=True)

        return Response(serializer.data)