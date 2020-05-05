from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'yourGold' not in request.session:
        request.session['counter'] = 0
    context = {
        'yourGold': 0,
    }
    return render(request, 'index.html', context)

def process_money(request):
    start = 10
    stop = 20
    if request.session in 'Cave':
        start = 5
        stop = 10
    if 'yourGold' not in request.session:
        request.session ['yourGold'] = 0
    request.session['yourGold'] += random.randrange(start, stop)
    return redirect('/')

    def reset(request):
        request.session.clear()
    return redirect('')