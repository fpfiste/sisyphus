import base64
import io
import os
from itertools import chain
from operator import attrgetter
import traceback
from cryptography.fernet import Fernet
from PIL import Image
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from rest_framework import viewsets, status, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
import json

import re
from rest_framework.views import APIView
from django.db.models import F
from main import settings
from .components import Invoice, DeliveryNote
from .components.docwriter.schedule import SchedulePDF
from .components.docwriter.storno import InvoiceCancellationDoc
from .components.levensteindistance import Levenshtein
from .serializers import *
import datetime as dt
from .components.docparser.ms_form_recognizer import FormRecognizer







class AssetAbsenceCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetAbsenceCodes.objects.all()
    serializer_class = AssetAbsenceCodeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = AssetAbsenceCodes.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class AssetAbsenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetAbsences.objects.all()
    serializer_class = AssetAbsenceSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = AssetAbsences.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data



class AssetTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetTypes.objects.all()
    serializer_class = AssetTypeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = AssetTypes.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Assets.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data
        #return data


class ConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Config.objects.all()
    serializer_class = CoinfigSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Config.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')

        return data
        #return data

    @action(methods=['POST'], detail=False)
    def setCompany(self, request):
        request.data._mutable = True

        request.data['fk_sys_rec_status'] = 1
        request.data['id_employee'] = 0

        try:
            instance = Companies.objects.get(id_company=0)
            srl = CompanySerializer(data=request.data, instance=instance)
        except Companies.DoesNotExist as e:
            srl = CompanySerializer(data=request.data)

        if srl.is_valid():
            srl.save()

            return Response(data={}, status=status.HTTP_200_OK)

        return Response(data={}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def setDocumentConf(self, request):



        content_type, binaries = request.data['file'].split(',')
        data = base64.b64decode(binaries)

        print(binaries)

        logo = ('doc_logo', content_type, data)
        logo_width = ('doc_logo_width', request.data['doc_logo_width'], None)
        logo_height = ('doc_logo_height', request.data['doc_logo_height'], None)
        logo_x_offset = ('doc_logo_x_offset', request.data['doc_logo_x_offset'], None)
        logo_y_offset = ('doc_logo_y_offset', request.data['doc_logo_y_offset'], None)

        params = [logo, logo_width, logo_height, logo_x_offset, logo_y_offset]


        for i in params:
            print(len(Config.objects.filter(config_key=i[0])))
            if len(Config.objects.filter(config_key=i[0])) == 0:
                cnf = Config(config_key=i[0], value_string=i[1], value_bytes=i[2])
                cnf.save()



            else:
                cnf = Config.objects.get(config_key=i[0])
                cnf.value_string = i[1]
                cnf.value_bytes = i[2]
                cnf.save()





        return Response(data={}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def setRecoginizerConfig(self, request):

        code_bytes = settings.SECRET_KEY.encode("utf-8")
        key = base64.urlsafe_b64encode(code_bytes.ljust(32)[:32])

        fernet = Fernet(key)



        key = fernet.encrypt(str.encode(request.data['key']))

        enpoint = ('ms_form_recoginizer_endpoint', request.data['endpoint'], None)
        key = ('ms_form_recognizer_key', key, key)


        params = [enpoint, key]


        for i in params:
            if len(Config.objects.filter(config_key=i[0])) == 0:
                cnf = Config(config_key=i[0], value_string=i[1], value_bytes=i[2])
                cnf.save()



            else:
                cnf = Config.objects.get(config_key=i[0])
                cnf.value_string = i[1]
                cnf.value_bytes = i[2]
                cnf.save()





        return Response(data={}, status=status.HTTP_200_OK)




class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        print(self.request.query_params)

        queryset = Companies.objects.all()

        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])


        data = queryset.filter(**params).order_by('-pk')

        return data


    @transaction.atomic
    def create(self, request):
        serializer = CompanySerializer(data=request.data)

        serializer.is_valid()

        print(serializer.errors)



        if not serializer.is_valid():
            return Response({'message': 'Something is wrong with your input'}, status=status.HTTP_400_BAD_REQUEST)


        try:
            with transaction.atomic():
                self.perform_create(serializer)

                if serializer.data['is_customer'] == True:
                    project_data = {
                            'fk_customer' : serializer.instance.pk,
                            'project_name' : request.data['company_name'] + ' - Default',
                            'start_date' : dt.datetime.now().strftime('%Y-%m-%d'),
                            'end_date' : '9999-12-31',
                            'fk_sys_rec_status' : 1
                    }




                    project_serializer = ProjectsSerializer(data=project_data)

                    project_serializer.is_valid()

                    if not project_serializer.is_valid():
                        return Response({'message': 'Something is wrong with your input'}, status=status.HTTP_400_BAD_REQUEST)

                    project_serializer.save()


                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)





class ClearingTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ClearingType.objects.all()
    serializer_class = ClearingTypeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = ClearingType.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data







class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Countries.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('pk')
        return data




class CurrencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Currencies.objects.all()
    serializer_class = CurrencySerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Currencies.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data




class EmployeeAbsenceCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeAbsenceCodes.objects.all()
    serializer_class = EmployeeAbsenceCodeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = EmployeeAbsenceCodes.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class EmployeeAbsenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeAbsences.objects.all()
    serializer_class = EmployeeAbsenceSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = EmployeeAbsences.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class EmployeeTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeTypes.objects.all()
    serializer_class = EmployeeTypeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = EmployeeTypes.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Employees.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data

    @action(methods=['GET'], detail=False)
    def get_active_user(self, request):
        user = AuthUser.objects.get(username=request.user)
        data = {'firstname' : user.first_name}
        return Response(data, status=status.HTTP_200_OK)



    @action(methods=['GET'], detail=False)
    def get_employee_by_username(self, request):
        try:
            user_id = AuthUser.objects.get(username=request.user).pk

            employee = Employees.objects.get(fk_user=user_id)

            srl = EmployeeSerializer(instance=employee)

            return Response(srl.data, status=status.HTTP_200_OK)
        except AuthUser.DoesNotExist:
            return Response({'message' : 'User Does Not Exist'}, status.HTTP_200_OK)
        except Employees.DoesNotExist:
            return Response({'message' : 'Employee Does Not Exist'}, status.HTTP_200_OK)



class InvoiceStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InvoiceStates.objects.all()
    serializer_class = InvoiceStateSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = InvoiceStates.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class InvoiceTermsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InvoiceTerms.objects.all()
    serializer_class = InvoiceTermsSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = InvoiceTerms.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data

class InvoiceTextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InvoiceTextTemplates.objects.all()
    serializer_class = InvoiceTextTemplatesSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = InvoiceTextTemplates.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class ReceivablesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Receivables.objects.all()
    serializer_class = ReceivablesSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Receivables.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data



    @transaction.atomic
    def create(self, request):
        try:
            sales = []
            tasks = []
            request.data._mutable = True



            print(request.data)
            if 'sales[]' in request.data and len(request.data['sales[]']) > 0:
                sales = Sales.objects.filter(id_sale__in=request.data.pop('sales[]'))
            if 'tasks[]' in request.data and len(request.data['tasks[]']) > 0:
                tasks = Tasks.objects.filter(id_task__in=request.data.pop('tasks[]'))

            if len(sales) == 0 and len(tasks) == 0:
                return Response({'message':'Can not create an invoice without tasks or sales to bill.'}, status=status.HTTP_400_BAD_REQUEST)

            request.data['fk_invoice_state'] = 1
            request.data['invoice_date'] = dt.date.today().strftime('%Y-%m-%d')
            request.data['discount'] = float(request.data['discount']) / 100 if request.data['discount'] != "" else 0.00

            with transaction.atomic():
                serializer = ReceivablesSerializer(data=request.data)

                if not serializer.is_valid():
                    print(serializer.errors)
                    return Response({'message': 'Something is wrong with your input'},
                                    status=status.HTTP_400_BAD_REQUEST)




                serializer.save()

                for sale in sales:
                    sale.fk_sales_status = SalesState.objects.get(id_sales_state=2)
                    sale.fk_invoice = serializer.instance
                    sale.save()

                for task in tasks:
                    task.fk_task_state = TaskStates.objects.get(id_task_state=5)
                    task.fk_invoice = serializer.instance
                    task.save()

                invoice = serializer.instance
                vat = Vat.objects.get(id_vat=request.data['fk_vat'])
                currency = Currencies.objects.get(id_currency=request.data['fk_currency'])
                terms = InvoiceTerms.objects.get(id_invoice_term=request.data['fk_invoice_terms'])
                project = Projects.objects.get(id_project=request.data['fk_project'])


                doc = Invoice(invoice.pk,  invoice.invoice_date, invoice.invoice_text, vat.vat, currency.currency_abbreviation, currency.currency_account_nr, terms.due_days, language='de',output_path=settings.TMP_FOLDER, discount=invoice.discount)

                doc.set_logo(logo=Config.objects.get(config_key='doc_logo').value_bytes,
                             logo_width=Config.objects.get(config_key='doc_logo_width').value_string,
                             logo_height=Config.objects.get(config_key='doc_logo_height').value_string,
                             logo_x=Config.objects.get(config_key='doc_logo_x_offset').value_string,
                             logo_y=Config.objects.get(config_key='doc_logo_y_offset').value_string
                             )

                customer = project.fk_customer

                doc.set_customer(customer.id_company, customer.company_name, customer.company_street, customer.company_zipcode,
                                 customer.company_city, customer.fk_country.country_code)

                company_detail = settings.COMPANY
                company_detail['agent'] = request.user

                doc.set_company(**company_detail)


                for task in tasks:
                    doc.add_position(
                        position_id=task.id_task,
                        date = task.task_date_to.strftime('%d.%m.%Y'),
                        reference_text=task.customer_reference,
                        description=task.description,
                        unit=task.fk_unit.unit,
                        amount=task.amount,
                        unit_price=task.unit_price,
                        pos_type='T'
                    )





                for sale in sales:
                    doc.add_position(
                        position_id=sale.id_sale,
                        date = sale.sale_date.strftime('%d.%m.%Y'),
                        reference_text=sale.customer_reference,
                        description=sale.description,
                        unit=sale.fk_unit.unit,
                        amount=sale.amount,
                        unit_price=sale.unit_price,
                        pos_type='S'
                    )
                net_total, total = doc.draw()

                invoice.net_total = net_total
                invoice.total = total
                invoice.fk_vat = vat
                invoice.fk_currency = currency
                invoice.fk_project = project
                invoice.save()
                url = '/static/tmp/' + os.path.basename(doc.file_name)

                return Response({'file_url': url}, status=status.HTTP_200_OK)
        except ValueError as v:
            print(v)
            return Response({'message': str(v)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message': 'Unknown Error'}, status=status.HTTP_400_BAD_REQUEST)







    @transaction.atomic
    def destroy(self, request, pk):
        try:

            instance = Receivables.objects.get(id_invoice=pk)

            if instance.fk_invoice_state.id_invoice_state >= 2:
                return Response({'message': 'Invoice was already booked'}, status=status.HTTP_403_FORBIDDEN)

            with ((transaction.atomic())):
                instance.fk_invoice_state = InvoiceStates.objects.get(id_invoice_state=4)


                tasks = Tasks.objects.filter(fk_invoice=pk)
                sales = Sales.objects.filter(fk_invoice=pk)

                positions = list(chain(tasks, sales))
                customer = positions[0].fk_project.fk_customer
                currency = positions[0].fk_currency.currency_abbreviation

                cancellation = Cancellations()
                cancellation.cancellation_date = dt.date.today()
                cancellation.cancellation_time = dt.datetime.now().time()
                cancellation.cancellation_reason = ''
                cancellation.cancellation_user = request.user
                cancellation.fk_invoice = instance
                #

                cancellation.save()
                instance.save()
                sales.update(fk_invoice=None, fk_sales_status=1)
                tasks.update(fk_invoice=None, fk_task_state=3)

                doc = InvoiceCancellationDoc(
                    cancellation.pk,
                    cancellation.cancellation_date ,
                    cancellation.cancellation_time,
                    cancellation.cancellation_reason,
                    settings.TMP_FOLDER,
                    instance.pk,
                    instance.invoice_date,
                    instance.fk_invoice_terms.term_title,
                    instance.fk_vat.vat_title,
                    instance.total,
                    instance.fk_currency.currency_abbreviation

                )

                doc.set_logo(logo=Config.objects.get(config_key='doc_logo').value_bytes,
                             logo_width=Config.objects.get(config_key='doc_logo_width').value_string,
                             logo_height=Config.objects.get(config_key='doc_logo_height').value_string,
                             logo_x=Config.objects.get(config_key='doc_logo_x_offset').value_string,
                             logo_y=Config.objects.get(config_key='doc_logo_y_offset').value_string
                             )

                doc.set_customer(customer.id_company, customer.company_name, customer.company_street, customer.company_zipcode,
                                 customer.company_city, customer.fk_country.country_code)




                company_detail = settings.COMPANY
                company_detail['agent'] = request.user

                doc.set_company(**company_detail)

                doc.draw()

                url = '/static/tmp/' + os.path.basename(doc.file_name)

                return Response({'file_url': url}, status=status.HTTP_200_OK)







            return Response(serializer.data)
        except Exception as e:
            print(traceback.format_exc())
            return Response({'message': 'Unknown error'}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['GET'])
    def pdf(self, request, pk):

        invoice = Receivables.objects.get(id_invoice=pk)
        vat = invoice.fk_vat
        currency = invoice.fk_currency
        terms = invoice.fk_invoice_terms
        customer = invoice.fk_project.fk_customer

        if invoice.fk_invoice_state.id_invoice_state == 4:
            cancellation = Cancellations.objects.get(fk_invoice=invoice)
            doc = InvoiceCancellationDoc(
                cancellation.pk,
                cancellation.cancellation_date,
                cancellation.cancellation_time,
                cancellation.cancellation_reason,
                settings.TMP_FOLDER,
                invoice.pk,
                invoice.invoice_date,
                invoice.fk_invoice_terms.term_title,
                invoice.fk_vat.vat,
                invoice.total,
                currency.currency_abbreviation
            )

            doc.set_logo(logo=Config.objects.get(config_key='doc_logo').value_bytes,
                         logo_width=Config.objects.get(config_key='doc_logo_width').value_string,
                         logo_height=Config.objects.get(config_key='doc_logo_height').value_string,
                         logo_x=Config.objects.get(config_key='doc_logo_x_offset').value_string,
                         logo_y=Config.objects.get(config_key='doc_logo_y_offset').value_string
                         )




            doc.set_customer(customer.id_company, customer.company_name, customer.company_street,
                             customer.company_zipcode,
                             customer.company_city, customer.fk_country.country_code)

            company_detail = settings.COMPANY
            company_detail['agent'] = request.user

            doc.set_company(**company_detail)

            doc.draw()
        else:
            tasks = Tasks.objects.filter(fk_invoice=invoice)
            sales = Sales.objects.filter(fk_invoice=invoice)

            positions = list(chain(tasks, sales))


            doc = Invoice(invoice.pk,
                          invoice.invoice_date,
                          invoice.invoice_text,
                          vat.vat,
                          currency.currency_abbreviation,
                          currency.currency_account_nr,
                          terms.due_days,
                          language='de',
                          output_path=settings.TMP_FOLDER,
                          discount=invoice.discount)

            doc.set_logo(logo=Config.objects.get(config_key='doc_logo').value_bytes,
                         logo_width=Config.objects.get(config_key='doc_logo_width').value_string,
                         logo_height=Config.objects.get(config_key='doc_logo_height').value_string,
                         logo_x=Config.objects.get(config_key='doc_logo_x_offset').value_string,
                         logo_y=Config.objects.get(config_key='doc_logo_y_offset').value_string
                         )



            doc.set_customer(customer.id_company, customer.company_name, customer.company_street, customer.company_zipcode,
                             customer.company_city, customer.fk_country.country_code)

            company_detail = settings.COMPANY
            company_detail['agent'] = request.user

            doc.set_company(**company_detail)

            for task in tasks:
                doc.add_position(
                    position_id=task.id_task,
                    date=task.task_date_to.strftime('%d.%m.%Y'),
                    reference_text=task.customer_reference,
                    description=task.description,
                    unit=task.fk_unit.unit,
                    amount=task.amount,
                    unit_price=task.unit_price,
                    pos_type='T'
                )

            for sale in sales:
                doc.add_position(
                    position_id=sale.id_sale,
                    date=sale.sale_date.strftime('%d.%m.%Y'),
                    reference_text=sale.customer_reference,
                    description=sale.description,
                    unit=sale.fk_unit.unit,
                    amount=sale.amount,
                    unit_price=sale.unit_price,
                    pos_type='S'
                )
            doc.draw()

        url = '/static/tmp/' + os.path.basename(doc.file_name)

        return Response({'file_url': url}, status=status.HTTP_200_OK)




class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):

        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Projects.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class SalesStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SalesState.objects.all()
    serializer_class = SalesStateSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = SalesState.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data

class SalesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)





    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Sales.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken' and key != 'invoice_text'])

        data = queryset.filter(**params).order_by('-pk')

        return data


    def create(self, request):

        request.data._mutable = True
        request.data['fk_sales_status'] = "1"


        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        request.data._mutable = True

        instance = Sales.objects.get(id_sale = pk)


        if instance.fk_sales_status.id_sales_state >= 2:
            return Response({'message': 'Sale was already billed'}, status=status.HTTP_403_FORBIDDEN)

        instance.fk_sales_status = SalesState.objects.get(id_sales_state=3)
        instance.save()

        serializer = self.get_serializer(instance)


        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def close(self, request,pk):
        sale = Sales.objects.get(id_sale=pk)
        if sale.sale_date != None and \
            sale.fk_project!= None and \
            sale.amount != None and \
            sale.unit_price != None and \
            sale.fk_unit != None and \
            sale.description != None and \
            sale.sale_time != None and \
            sale.fk_currency != None and \
            sale.fk_vat != None:

            sale.fk_sales_status = SalesState.objects.get(id_sales_state = 2)
            sale.save()
            serializer = SalesSerializer(instance=sale)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Sale can not be closed due to missing data'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def pdf(self, request, pk):

        doc = DeliveryNote('de', output_path=settings.TMP_FOLDER)

        doc.set_logo(logo=Config.objects.get(config_key='logo').value_bytes,
                     logo_width=Config.objects.get(config_key='logo_width').value_string,
                     logo_height=Config.objects.get(config_key='logo_height').value_string,
                     logo_x=Config.objects.get(config_key='logo_x_offset').value_string,
                     logo_y=Config.objects.get(config_key='logo_y_offset').value_string
                     )

        sale = Sales.objects.get(pk=pk)
        customer = sale.fk_project.fk_customer

        doc.set_customer(10, customer.company_name, customer.company_street, customer.company_zipcode, customer.company_city, customer.fk_country.country_code)

        company_detail = settings.COMPANY
        company_detail['agent'] = request.user


        doc.set_company(**company_detail)

        doc.add_position(
            sale.id_sale,
            sale.sale_date,
            sale.sale_time,
            sale.description,
            sale.fk_unit.unit,
            sale.amount,

            sale.customer_reference

        )

        doc.draw()

        url = '/static/tmp/' + os.path.basename(doc.file_name)

        return Response({'file_url': url}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def getoverview(self, request):
        sales = Sales.objects.filter(fk_sales_status=1, fk_clearing_type=2)

        data = {

            'to_bill': len(sales)

        }

        return Response(data, status=status.HTTP_200_OK)

class SysRecStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SysRecStates.objects.all()
    serializer_class = SysRecStatesSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = SysRecStates.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data

class TaskStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TaskStates.objects.all()
    serializer_class = TaskStateSerializer

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        planned_tasks = Tasks.objects.filter(fk_task_state = 2)
        timestamp = dt.datetime.now()

        for i in planned_tasks:
            task_ts = dt.datetime.combine(i.task_date_to, i.task_time_to)

            if task_ts < timestamp:
                i.fk_task_state = TaskStates.objects.get(id_task_state=3)


        queryset = TaskStates.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data




class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Templates.objects.all()
    serializer_class = TemplateSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Templates.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data
class TemplateTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TemplateTypes.objects.all()
    serializer_class = TemplateTypeSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = TemplateTypes.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data




class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    

    def retrieve(self, request, pk):
        task = Tasks.objects.get(id_task=pk)

        if task.task_date_to != None and task.task_time_to != None and task.fk_task_state.id_task_state == 2:
            ts_task = dt.datetime.combine(task.task_date_to, task.task_time_to)
            ts_now = dt.datetime.now()

            if ts_task < ts_now:
                task.fk_task_state = TaskStates.objects.get(id_task_state = 3)
                task.save()
        serializer = TaskSerializer(instance=task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        print(self.request.query_params)
        tasks = Tasks.objects.filter(fk_task_state__id_task_state=2)

        for task in tasks:
            if task.task_date_to != None and task.task_time_to != None and task.fk_task_state.id_task_state == 2:
                ts_task = dt.datetime.combine(task.task_date_to, task.task_time_to)
                ts_now = dt.datetime.now()

                if ts_task < ts_now:
                    task.fk_task_state = TaskStates.objects.get(id_task_state=3)
                    task.save()

        queryset = Tasks.objects.all()

        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken' and key != 'invoice_text'])

        if 'limit' in params:
            limit = params.pop('limit')
        else:
            limit = 20

        data = queryset.filter(**params).order_by('-pk')[:limit]


        return data

    def create(self, request):

        request.data._mutable = True

        date_from = request.data.get('task_date_from')
        date_to = request.data.get('task_date_to')
        time_from = request.data.get('task_time_from')
        time_to = request.data.get('task_time_to')
        employee = request.data.get('fk_employee_1')
        state = request.data.get('fk_task_state')



        if (date_from != '') and (date_to != '') and (time_from != '') and (time_to != '') and (employee != ''):
            request.data['fk_task_state'] = "2"

            end_ts = dt.datetime.strptime(date_to + ' ' + time_to[:5], '%Y-%m-%d %H:%M')
            current_ts = dt.datetime.now()

            if end_ts < current_ts:

                request.data['fk_task_state'] = "3"
        else:
            request.data['fk_task_state'] = "1"


        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request,pk):
        request.data._mutable = True
        task = Tasks.objects.get(id_task = pk)


        data = request.data.dict()
        date_from = request.data.get('task_date_from')
        date_to = request.data.get('task_date_to')
        time_from = request.data.get('task_time_from')
        time_to = request.data.get('task_time_to')
        employee = request.data.get('fk_employee_1')
        state = request.data.get('fk_task_state')


        if task.fk_task_state.id_task_state < 4:
            if (date_from != '') and (date_to != '') and (time_from != '') and (time_to != '') and (employee != ''):
                request.data['fk_task_state'] = "2"

                end_ts = dt.datetime.strptime(date_to + ' ' + time_to[:5], '%Y-%m-%d %H:%M')
                current_ts = dt.datetime.now()

                if end_ts < current_ts:

                    request.data['fk_task_state'] = "3"
            else:
                request.data['fk_task_state'] = "1"



            serializer = self.get_serializer(task, data=request.data)

            serializer.is_valid(raise_exception=True)

            self.perform_update(serializer)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'message' : 'Task was already closed or billed and cannot be updated anymore'}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk):
        request.data._mutable = True


        request.data['fk_task_state'] = "-1"
        instance = Tasks.objects.get(id_task = pk)


        if instance.fk_task_state_id >= 4:
            return Response({'message': 'Task already billed'}, status=status.HTTP_403_FORBIDDEN)

        instance.fk_task_state = TaskStates.objects.get(id_task_state=6)
        instance.save()

        serializer = self.get_serializer(instance)



        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def listday(self, request):
        date = request.query_params.get('date')

        if date == None:
            date =  dt.date.today().strftime("%Y-%m-%d")

        tasks = Tasks.objects.filter(
                Q(task_date_from=date) |
                Q(task_date_to=date) |
                Q(task_date_from__lt= date, task_date_to__gt= date)


        )
        tasks = tasks.filter(
            Q(fk_employee_1__isnull=False)
        )
        tasks = tasks.filter(task_time_from__isnull=False, task_time_to__isnull=False).exclude(fk_task_state=6).order_by('task_date_from', 'task_time_from')

        serializer = self.get_serializer(tasks, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def getOpenTasks(self, request):

        tasks = Tasks.objects.filter(
            Q(task_date_from__isnull=True) |
            Q(task_date_to__isnull=True) |
            Q(fk_employee_1__isnull=True)
        ).order_by('id_task')

        tasks = tasks.filter(fk_task_state__gt=0)

        serializer = self.get_serializer(tasks, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def close(self, request,pk):
        request.data._mutable = True

        request.data['fk_task_state'] = 4


        if (request.data['id_task'] not in ('', None) and \
            request.data['fk_project'] not in ('', None) and \
            request.data['description']not in ('', None) and \
            request.data['amount'] not in ('', None) and \
            request.data['unit_price'] not in ('', None) and \
            request.data['fk_currency'] not in ('', None) and \
            request.data['fk_employee_1'] not in ('', None) and \
            request.data['fk_unit'] not in ('', None) and \
            request.data['fk_vat'] not in ('', None) and \
            request.data['fk_clearing_type'] not in ('', None) ):

            task = Tasks.objects.get(id_task=pk)
            serializer = self.get_serializer(task, data=request.data)

            serializer.is_valid(raise_exception=True)

            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Task can not be closed due to missing data'},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def pdf(self, request, pk):

        doc = DeliveryNote('de', output_path=settings.TMP_FOLDER)

        doc.set_logo(logo=Config.objects.get(config_key='logo').value_bytes,
                     logo_width=Config.objects.get(config_key='logo_width').value_string,
                     logo_height=Config.objects.get(config_key='logo_height').value_string,
                     logo_x=Config.objects.get(config_key='logo_x_offset').value_string,
                     logo_y=Config.objects.get(config_key='logo_y_offset').value_string
                     )


        task = Tasks.objects.get(pk=pk)
        customer = task.fk_project.fk_customer

        doc.set_customer(10, customer.company_name, customer.company_street, customer.company_zipcode, customer.company_city, customer.fk_country.country_code)

        company_detail = settings.COMPANY
        company_detail['agent'] = request.user


        doc.set_company(**company_detail)

        doc.add_position(
            task.id_task,
            task.task_date_to,
            task.task_time_to,
            task.description,
            task.fk_unit.unit,
            task.amount,

            task.customer_reference

        )

        doc.draw()

        url = '/static/tmp/' + os.path.basename(doc.file_name)

        return Response({'file_url': url}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def printSchedule(self, request):
        date = request.query_params.get('date')

        if date == None:
            return Response({'message': 'No date was specified'}, status=status.HTTP_400_BAD_REQUEST)

        tasks = Tasks.objects.filter(
            Q(task_date_from=date) |
            Q(task_date_to=date) |
            Q(task_date_from__lt=date, task_date_to__gt=date)

        )

        tasks = tasks.filter(fk_employee_1__isnull=False, task_time_from__isnull=False,
                             task_time_to__isnull=False).order_by('task_date_from', 'task_time_from')

        doc = SchedulePDF(date, 'ch', output_path=settings.TMP_FOLDER)

        for task in tasks:

            if task.fk_employee_1 != None:
                doc.add_employee(task.fk_employee_1.id_employee, task.fk_employee_1.employee_internal_alias)
            if task.fk_employee_2 != None:
                doc.add_employee(task.fk_employee_2.id_employee, task.fk_employee_2.employee_internal_alias)

            doc.add_task(
                task.id_task,
                task.description,
                task.task_date_from,
                task.task_time_from,
                task.task_date_to,
                task.task_time_to,
                task.fk_employee_1.id_employee if task.fk_employee_1 != None else None,
                task.fk_employee_2.id_employee if task.fk_employee_2 != None else None,
                task.fk_asset_1.id_asset if task.fk_asset_1 != None else None,
                task.fk_asset_2.id_asset if task.fk_asset_1 != None else None,
            )


        doc.draw()
        url = '/static/tmp/' + os.path.basename(doc.file_name)

        return Response({'file_url': url}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def getoverview(self, request):
        tasks = Tasks.objects.filter(fk_task_state__lt=5)


        data = {
            'open': len(tasks.filter(fk_task_state=1)),
            'scheduled': len(tasks.filter(fk_task_state=2)),
            'executed': len(tasks.filter(fk_task_state=3)),
            'to_bill': len(tasks.filter(fk_task_state=4, fk_clearing_type=2))

        }

        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_ongoing_tasks(self, request):
        ts = dt.datetime.now()

        date = ts.date()
        time = ts.time()
        tasks = Tasks.objects.filter(task_date_from__lte=date, task_time_from__lte=time, task_date_to__gte=date, task_time_to__gte=time)

        srl = TaskSerializer(data=tasks)

        return Response(srl.data, status=status.HTTP_200_OK)

class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Units.objects.all()
    serializer_class = UnitSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Units.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class VATViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vat.objects.all()
    serializer_class = VATSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Vat.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')
        return data


class PayablesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Payables.objects.all()
    serializer_class = PayableSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Payables.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != '' and key != 'csrfmiddlewaretoken'])
        data = queryset.filter(**params).order_by('-pk')

        print(data)
        return data



    def create(self, request):
        request.data._mutable = True

        request.data['fk_invoice_status'] = 1

        srl = PayableSerializer(data=request.data)

        if srl.is_valid():
            srl.save()
            return Response({'data': srl.data}, status=status.HTTP_200_OK)
        else:
            print(srl.errors)
            return Response({'message': 'Something is wrong'}, status=status.HTTP_404_NOT_FOUND)





    @action(detail=False, methods=['POST'])
    def extract_data(self, request):
        print(request.data)

        endpoint = Config.objects.get(config_key='ms_form_recoginizer_endpoint')
        key = Config.objects.get(config_key='ms_form_recognizer_key')


        key_string = bytes(key.value_bytes).decode("utf-8")
        secret_key = settings.SECRET_KEY.encode("utf-8")
        secret_key = base64.urlsafe_b64encode(secret_key.ljust(32)[:32])

        fernet = Fernet(secret_key)

        key = fernet.decrypt(key_string).decode('utf-8')

        rec = FormRecognizer(endpoint.value_string, key)

        pdf = request.FILES['file'].open()
        data = rec.analyse_invoice(pdf)
        print(data)

        vendor = re.sub(r'\W+', '', data['vendor_name'])
        comp = Companies.objects.annotate(lev_dist=Levenshtein(F('company_name'), vendor)).order_by('lev_dist')

        terms = data['payment_term']

        if data['invoice_date'] != None and data['due_date'] != None:
            due_days = (data['due_date'] - data['invoice_date']).days + 1
        elif data['invoice_date'] == None :
            data['invoice_date'] = ''
        elif data['due_date'] == None:
            due_days = 30



        if data['invoice_total'] != None and data['net_total'] != None and  data['tax'] != None:
            currency = Currencies.objects.filter(currency_abbreviation=data['invoice_total']['value']['code'])

            net_total = data['net_total']['value']['amount']
            tax = data['tax']['value']['amount']
            total = data['invoice_total']['value']['amount']



        elif data['invoice_total'] == None and data['net_total'] != None and  data['tax'] != None:
            currency = Currencies.objects.filter(currency_abbreviation=data['net_total']['value']['code'])

            net_total = data['net_total']['value']['amount']
            tax = data['tax']['value']['amount']
            total = net_total + tax



        elif data['invoice_total'] != None and data['net_total'] == None and  data['tax'] != None:
            currency = Currencies.objects.filter(currency_abbreviation=data['invoice_total']['value']['code'])

            total = data['invoice_total']['value']['amount']
            tax = data['tax']['value']['amount']
            net_total = total - tax


        elif data['invoice_total'] != None and data['net_total'] != None and  data['tax'] == None:
            currency = Currencies.objects.filter(currency_abbreviation=data['invoice_total']['value']['code'])

            net_total = data['net_total']['value']['amount']
            total = data['invoice_total']['value']['amount']
            tax = total - net_total

        else:
            net_total = data['net_total']['value']['amount']
            total = data['invoice_total']['value']['amount']
            tax = data['tax']['value']['amount']
            currency = []

        response = {

            'fk_company' : comp[0].id_company if len(comp) > 0 else '',
            'invoice_nr': data['invoice_nr'],
            'fk_terms' : InvoiceTerms.objects.filter(due_days__lte=due_days).order_by('-due_days')[0].id_invoice_term,
            'invoice_date' : data['invoice_date'],
            'fk_currency' : currency[0].id_currency if len(currency) > 0 else '',
            'vat' : float(tax),
            'net_total' : float(net_total),
            'total' : float(total),
            'positions': data['items']
        }



        return Response(response, status=status.HTTP_200_OK)














