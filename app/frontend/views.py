import json
from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
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
def render_home(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)





def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def send_config(request):
    return  JsonResponse(config)


def login_view(request):
    request.session['push_sent'] = None
    form = AuthenticationForm()
    url = request.path
    page_config = config['pages'][url]
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

    return render(request, 'frontend/pages/login.html', {'login_form': form, 'page_config':page_config})






@permission_required('api.add_tasks', '/errors/403')
@permission_required('api.view_tasks', '/errors/403')
@permission_required('api.change_tasks', '/errors/403')
@permission_required('api.delete_tasks', '/errors/403')
def render_schedule(request, pk=None):

    user = User.objects.get(username=request.user)


    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_projects','/errors/403' )
@permission_required('api.view_projects', '/errors/403')
@permission_required('api.change_projects', '/errors/403')
@permission_required('api.delete_projects', '/errors/403')
def render_projects(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_tasks', '/errors/403')
@permission_required('api.view_tasks', '/errors/403')
@permission_required('api.change_tasks', '/errors/403')
@permission_required('api.delete_tasks', '/errors/403')
def render_tasks(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_sales', '/errors/403')
@permission_required('api.view_sales', '/errors/403')
@permission_required('api.change_sales', '/errors/403')
@permission_required('api.delete_sales', '/errors/403')
def render_sales(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_companies', '/errors/403')
@permission_required('api.view_companies', '/errors/403')
@permission_required('api.change_companies', '/errors/403')
@permission_required('api.delete_companies', '/errors/403')
def render_companies(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_employees', '/errors/403')
@permission_required('api.view_employees', '/errors/403')
@permission_required('api.change_employees', '/errors/403')
@permission_required('api.delete_employees', '/errors/403')
def render_employees(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_assets', '/errors/403')
@permission_required('api.view_assets', '/errors/403')
@permission_required('api.change_assets', '/errors/403')
@permission_required('api.delete_assets', '/errors/403')
def render_assets(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)

@permission_required('api.add_templates', '/errors/403')
@permission_required('api.view_templates', '/errors/403')
@permission_required('api.change_templates', '/errors/403')
@permission_required('api.delete_templates', '/errors/403')
def render_templates(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)


@permission_required('api.add_paymentconditions', '/errors/403')
@permission_required('api.view_paymentconditions', '/errors/403')
@permission_required('api.change_paymentconditions', '/errors/403')
@permission_required('api.delete_paymentconditions', '/errors/403')
def render_terms(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)





@permission_required('api.add_receivables', '/errors/403')
@permission_required('api.view_receivables', '/errors/403')
@permission_required('api.change_receivables', '/errors/403')
@permission_required('api.delete_receivables', '/errors/403')
def render_invoices(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)



@permission_required('api.add_receivables', '/errors/403')
@permission_required('api.view_tasks', '/errors/403')
def render_billing(request, pk=None):
    url = request.path.split('/' + str(pk))[0]

    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)





@permission_required('api.add_payables', '/errors/403')
@permission_required('api.add_payables', '/errors/403')
@permission_required('api.add_payables', '/errors/403')
@permission_required('api.add_payables', '/errors/403')
def render_payables(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    data = {'page_config': page_config}
    return render(request, page_config['template'], data)





@login_required()
def render_settings(request,pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    user_detail = User.objects.get(username=request.user)
    data = {'page_config': page_config,
            'user': user_detail}
    return render(request, page_config['template'], data)

@login_required()
def render_403(request,pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    user_detail = User.objects.get(username=request.user)
    data = {'page_config': page_config,
            'user': user_detail}
    return render(request, page_config['template'], data)




