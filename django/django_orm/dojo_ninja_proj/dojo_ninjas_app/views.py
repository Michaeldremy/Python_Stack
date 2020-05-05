from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'addDojo': Dojos.objects.all(),
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    Dojos.objects.create (name=request.POST['name'],city=request.POST['city'],state=request.POST['state'])
    return(redirect('/'))

def add_ninja(request):
    this_dojo = Dojos.objects.get(name=request.POST['dojo_dropdown'])
    Ninjas.objects.create (first_name=request.POST['first_name'],last_name=request.POST['last_name'],dojo_id=this_dojo)
    return(redirect('/'))