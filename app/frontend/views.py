import json
from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime as dt
import os
import copy

with open('app/frontend/static/config.json') as cnf:
    config = json.load(cnf)
@login_required
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

    return render(request, 'frontend/pages/login.html', {'login_form': form})


@permission_required('frontend.add_tasks', raise_exception=True)
@permission_required('frontend.view_tasks', raise_exception=True)
@permission_required('frontend.change_tasks', raise_exception=True)
@permission_required('frontend.delete_tasks', raise_exception=True)
@permission_required('frontend.add_employee_absences', raise_exception=True)
@permission_required('frontend.add_employee_absences', raise_exception=True)
@permission_required('frontend.add_employee_absences', raise_exception=True)
@permission_required('frontend.add_employee_absences', raise_exception=True)
@permission_required('frontend.add_asset_absences', raise_exception=True)
@permission_required('frontend.add_asset_absences', raise_exception=True)
@permission_required('frontend.add_asset_absences', raise_exception=True)
@permission_required('frontend.add_asset_absences', raise_exception=True)
def render_schedule(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('frontend.add_projects', raise_exception=True)
@permission_required('frontend.view_projects', raise_exception=True)
@permission_required('frontend.change_projects', raise_exception=True)
@permission_required('frontend.delete_projects', raise_exception=True)
def render_projects(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('frontend.add_tasks', raise_exception=True)
@permission_required('frontend.view_tasks', raise_exception=True)
@permission_required('frontend.change_tasks', raise_exception=True)
@permission_required('frontend.delete_tasks', raise_exception=True)
def render_tasks(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('frontend.add_sales', raise_exception=True)
@permission_required('frontend.view_sales', raise_exception=True)
@permission_required('frontend.change_sales', raise_exception=True)
@permission_required('frontend.delete_sales', raise_exception=True)
def render_sales(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('frontend.add_companies', raise_exception=True)
@permission_required('frontend.view_companies', raise_exception=True)
@permission_required('frontend.change_companies', raise_exception=True)
@permission_required('frontend.delete_companies', raise_exception=True)
def render_companies(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('frontend.add_employees', raise_exception=True)
@permission_required('frontend.view_employees', raise_exception=True)
@permission_required('frontend.change_employees', raise_exception=True)
@permission_required('frontend.delete_employees', raise_exception=True)
def render_employees(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('frontend.add_assets', raise_exception=True)
@permission_required('frontend.view_assets', raise_exception=True)
@permission_required('frontend.change_assets', raise_exception=True)
@permission_required('frontend.delete_assets', raise_exception=True)
def render_assets(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('frontend.add_task_templates', raise_exception=True)
@permission_required('frontend.view_task_templates', raise_exception=True)
@permission_required('frontend.change_task_templates', raise_exception=True)
@permission_required('frontend.delete_task_templates', raise_exception=True)
def render_task_templates(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('frontend.add_paymentconditions', raise_exception=True)
@permission_required('frontend.view_paymentconditions', raise_exception=True)
@permission_required('frontend.change_paymentconditions', raise_exception=True)
@permission_required('frontend.delete_paymentconditions', raise_exception=True)
def render_terms(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('frontend.add_invoices', raise_exception=True)
@permission_required('frontend.view_invoices', raise_exception=True)
@permission_required('frontend.change_invoices', raise_exception=True)
@permission_required('frontend.delete_invoices', raise_exception=True)
def render_invoices(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('frontend.add_invoices', raise_exception=True)
@permission_required('frontend.view_tasks', raise_exception=True)
def render_billing(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)



