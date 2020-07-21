from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('placeholder string where we will put list of blogs')

def new(request):
    return HttpResponse('placeholder string where we will put a form')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse('placeholder string to display blog ' + str(number))

def edit(request, number):
    return HttpResponse('placeholder string to edit blog ' + str(number))

def destroy(request, number):
    # do something with blog number 
    return redirect('/blogs')

def json(request):
    return JsonResponse({
        'title': 'My First Blog',
        'content': 'asl;dkfjaw woeifj oawwoeif jiii'
    })
