from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime as dt

import copy
from .config import pages, fields


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

    return render(request, 'frontend/pages/login.html', {'login_form': form})

def render_template(request, pk=None):
    #user = AuthUser.objects.get(id=request.user.id)
    #language = user.fk_language.language_abbreviation.lower()

    url = request.path.split('/' + str(pk))[0]
    page_config = copy.deepcopy(pages[url])

    for component, value in page_config['fields'].items():
        component_fields = []
        for element in value:
            component_fields.append(fields[element]['en'])
        page_config['fields'][component] = component_fields

    data = {'form': None, 'page_config':page_config}

    if not pk:
        return render(request, page_config['template'], data)
    else:
        return render(request, page_config['detail_template'], data)


