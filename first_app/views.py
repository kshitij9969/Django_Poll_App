# Create your views here.

import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, send_mass_mail, mail_admins, mail_managers, EmailMessage
from django.views.generic import ListView, TemplateView
from first_app.forms import *
from django.template import RequestContext
from first_app.models import *
from django.views.generic import ListView


class PollList(ListView):
    model = Polls
    template_name = 'viewpolls.html'
    context_object_name = 'poll_list'


def login(request):
    username = ''
    if request.method == 'POST':
        logindata = LoginForm(request.POST)
        if logindata.is_valid():
            username = logindata['username']
            password = logindata['password']
            user = UserProfile()
            user = user.createuser(username = username, password = password)
            user.save()
            # password = logindata.cleaned_data['password']
            # dbuser = UserProfile.objects.filter(username = username)
            # if not dbuser:
            #     logindata = LoginForm()
            # else:
            #     request.session['username'] = username
        else:
            logindata = LoginForm()

    return render(request, 'loggedin.html', {"username" : username})


def formview(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'loggedin.html', locals())
    else:
        return render(request, 'login.html', locals())
