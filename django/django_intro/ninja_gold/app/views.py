from django.shortcuts import render, redirect
import random
import math

# Create your views here.
def index(request):
    context = {
        'gold': request.session['gold']
    }
    return render(request, 'index.html', context)

def farm(request):
    gold = 10 + math.trunc((random.random()*11))
    print(gold)
    addGold(request, gold)
    print('Current Gold', request.session['gold'])
    return redirect('/')

def cave(request):
    gold = 5 + math.trunc((random.random()*6))
    print(gold)
    addGold(request, gold)
    print('Current Gold', request.session['gold'])
    return redirect('/')

def house(request):
    gold = 2 + math.trunc((random.random()*4))
    print(gold)
    addGold(request, gold)
    print('Current Gold', request.session['gold'])
    return redirect('/')

def casino(request):
    gold = -50 + math.trunc((random.random()*100))
    print(gold)
    addGold(request, gold)
    print('Current Gold', request.session['gold'])
    return redirect('/')

def addGold(request, gold):
    if 'gold' in request.session:
        print('Theres gold!')
        request.session['gold'] = request.session['gold'] + gold
    else:
        print('No gold!')
        print('Creating gold!')
        request.session['gold'] = gold
        