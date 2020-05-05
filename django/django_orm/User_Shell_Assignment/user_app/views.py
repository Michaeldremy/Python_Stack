from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'myUser': Users.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
    Users.objects.create (first_name=request.POST['first_name'],last_name=request.POST['last_name'],email_address=request.POST['email'],age=request.POST['age'])
    return redirect('/')