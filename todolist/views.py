import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist_item = Task.objects.all()
    context = {
        'list_item': data_todolist_item,
        'name': 'Azra',
    }
    return render(request, "todolist.html", context)