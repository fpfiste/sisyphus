import json
from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime as dt
import os


dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(dir_path, 'config.json')
with open(config_path) as cnf:
    config = json.load(cnf)
@login_required
def index(request):
        return render(request, 'frontend/home.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def send_config(request):
    return  JsonResponse(config)


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

    return render(request, 'frontend/pages/login.html', {'login_form': form})



def render_schedule(request, pk=None):

    user = User.objects.get(username=request.user)


    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_projects', )
@permission_required('api.view_projects', )
@permission_required('api.change_projects', )
@permission_required('api.delete_projects', )
def render_projects(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_tasks', )
@permission_required('api.view_tasks', )
@permission_required('api.change_tasks', )
@permission_required('api.delete_tasks', )
def render_tasks(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_sales', )
@permission_required('api.view_sales', )
@permission_required('api.change_sales', )
@permission_required('api.delete_sales', )
def render_sales(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_companies', )
@permission_required('api.view_companies', )
@permission_required('api.change_companies', )
@permission_required('api.delete_companies', )
def render_companies(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_employees', )
@permission_required('api.view_employees', )
@permission_required('api.change_employees', )
@permission_required('api.delete_employees', )
def render_employees(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_assets', )
@permission_required('api.view_assets', )
@permission_required('api.change_assets', )
@permission_required('api.delete_assets', )
def render_assets(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_task_templates', )
@permission_required('api.view_task_templates', )
@permission_required('api.change_task_templates', )
@permission_required('api.delete_task_templates', )
def render_task_templates(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_sales_templates', )
@permission_required('api.view_sales_templates', )
@permission_required('api.change_sales_templates', )
@permission_required('api.delete_sales_templates', )
def render_sales_templates(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    print(url)
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_paymentconditions', )
@permission_required('api.view_paymentconditions', )
@permission_required('api.change_paymentconditions', )
@permission_required('api.delete_paymentconditions', )
def render_terms(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_invoices', )
@permission_required('api.view_invoices', )
@permission_required('api.change_invoices', )
@permission_required('api.delete_invoices', )
def render_invoices(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_invoices', )
@permission_required('api.view_tasks',)
def render_billing(request, pk=None):
    url = request.path.split('/' + str(pk))[0]

    print(url)
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)



