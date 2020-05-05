from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    random = get_random_string(length=14)
    context = {
        'counter': 0,
        'random_word': random
    }
    return render(request, 'random.html', context)
    
def count(request):
    if 'counter' not in request.session:
        request.session ['counter'] = 0
    request.session['counter'] += 1
    return redirect('/random_word')

def reset(request):
    request.session.clear()
    return redirect('/random_word')