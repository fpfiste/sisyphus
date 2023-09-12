import json
from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime as dt
import os
import copy



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


    with open('app/frontend/static/config.json') as cnf:
        config = json.load(cnf)

    page_config = config['pages'][url]
    data = {'page_config':page_config}


    return render(request, page_config['template'], data)



