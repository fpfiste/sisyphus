import glob
import json
from http.client import HTTPResponse

from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User, Permission
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import datetime as dt
import os
from .templatetags.cachebreaker import break_cache

dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(dir_path, 'config.json')
with open(config_path) as cnf:
    config = json.load(cnf)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def send_config(request):
    return  JsonResponse(config)

@login_required()
def list_media(request):
    files = sorted(glob.glob(settings.MEDIA_ROOT + '/*'))

    files = ['/media' + f.split('/media')[-1] for f in files]

    data = {
        'data': files
    }
    return JsonResponse(data)



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

    return render(request, 'frontend/pages/login.html', {'login_form': form, 'page_config':page_config, 'cache_broken_js' : break_cache(page_config['js'])})


def check_permissions(request, required_permissions):
    user_permissions = request.user.get_user_permissions()
    group_permissions = request.user.get_group_permissions()

    for permission in required_permissions:
        if permission in user_permissions or permission in group_permissions:
            continue
        else:
            return False
    return True


@login_required()
def render_page(request, pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]

    user = request.user
    allowed = check_permissions(request, page_config['required_permissions'])

    if not allowed:
        return redirect('/errors/403')

    data = {'page_config': page_config,
            'cache_broken_js' : break_cache(page_config['js'])
    }
    return render(request, page_config['template'], data)


@login_required()
def render_403(request,pk=None):
    url = request.path.split('/' + str(pk))[0]
    page_config = config['pages'][url]
    user_detail = User.objects.get(username=request.user)
    data = {'page_config': page_config,
            'user': user_detail}
    return render(request, page_config['template'], data)






