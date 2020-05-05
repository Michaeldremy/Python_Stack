from django.shortcuts import HttpResponse, redirect, render
from time import gmtime, strftime

def index(request):
    return render(request, 'fruits.html')

def checkout(request):
    #count = int(form_strawberry), + int(form_raspberry), + int(apple_form)
    #customer = form_name
    context = {
        "fruit_one_from_form": request.POST['form_strawberry'],
        "fruit_two_from_form": request.POST['form_raspberry'],
        "fruit_three_from_form": request.POST['form_apple'],
        "form_name": request.POST['form_name'],
        "form_student_ID_num": request.POST['form_student_ID'],
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }    
    #print(f"Charging {customer_name} for {count}") need to work on this later
    #print(f"Charging {customer} for {total} fruits")
    return render(request, "checkout.html", context)

def time(request):
    context_one = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'checkout.html', context_one)