from http.client import HTTPResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime as dt
from .forms import *
from .config import pages


# Create your views here.
def index(request):

        return render(request, 'frontend/home.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def login_view(request):
    request.session['push_sent'] = None
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                request.session['last_activity']= dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                request.session['push_sent'] = None
                login(request, user)
                return redirect(reverse('index'))
    print('here')
    return render(request, 'frontend/pages/login.html', {'login_form': form})

def organizations(request):
    form = CompanyForm()
    data = {'form':form, 'page_config': pages['comapanies']}
    return render(request, 'frontend/pages/overview_table.html', data)

def organization_detail(request, id_company):
    print(request)
    form = CompanyForm()
    data = {'title': 'Companies', 'url':'company', 'form':form, 'id_company':id_company}
    return render(request, 'frontend/pages/organization_profile.html', data)

def projects(request):
    form = ProjectForm()
    data = {'form':form, 'page_config': pages['projects']}
    return render(request, 'frontend/pages/overview_table.html', data)

def project_detail(request, id_project):
    print(request)
    form = ProjectForm()
    data = {'title': 'Companies', 'url':'project', 'form':form, 'id_project':id_project}
    return render(request, 'frontend/pages/project_profile.html', data)


def tasks(request):
    form = TaskForm()
    data = {'title': 'Tasks', 'url':'project/task', 'form':form}
    return render(request, 'frontend/pages/overview_table.html', data)

def sales(request):
    form = SalesForm()
    data = {'title': 'Tasks', 'url':'project/sales', 'form':form}
    return render(request, 'frontend/pages/overview_table.html', data)

def employees(request):
    form = EmployeeForm()
    data = {'title': 'Tasks', 'url':'employee', 'form':form}
    return render(request, 'frontend/pages/overview_table.html', data)

def assets(request):
    form = AssetForm()
    data = {'title': 'Tasks', 'url':'asset', 'form':form}
    return render(request, 'frontend/pages/overview_table.html', data)

def invoices(request):
    form = InvoiceForm()
    data = {'title': 'Tasks', 'url':'invoice', 'form':form}
    return render(request, 'frontend/pages/overview_table.html', data)