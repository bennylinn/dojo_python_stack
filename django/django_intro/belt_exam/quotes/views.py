from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Login/Registration Page
def index(request):
    return render(request, 'index.html')

# Quotes Home Page
def quotes(request):
    current_user = User.objects.get(id=request.session['id'])
    context = {
        'name': current_user.first_name,
        'quotes': Quotes.objects.all(),
        'currentid': request.session['id']
    }

    return render(request, 'quotes.html', context) #add context for user-specific login

# Register/Validation
def register(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = User.objects.registration_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the login page 
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        newUser = User.objects.create(first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        email=request.POST['email'],
                                        password_hash=pw_hash)
        # redirect to a success route
        request.session['id'] = newUser.id
        return redirect('/quotes')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0 and user:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        logged_user = user[0]
        request.session['id'] = logged_user.id
        return redirect('/quotes')


def logout(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
    else:
        return redirect('/')

# creating new post
def create(request):
    author = request.POST['author']
    quote = author + ': ' + "'" + request.POST['quote'] + "'"
    user = User.objects.get(id=request.session['id'])

    errors = Quotes.objects.quote_validator(request.POST)

    # validation
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Quotes.objects.create(entry=quote, user=user)
    
    return redirect('/quotes')


# delete
def delete(request):
    quote_id = request.POST['quote_id']
    quote = Quotes.objects.get(id=quote_id)
    quote.delete()

    return redirect('/quotes')

def like(request):
    quote_id = request.POST['quotee_id']
    quote = Quotes.objects.get(id=quote_id)
    likes = quote.likes.all()

    current_user_id = request.session['id']
    current_user = User.objects.get(id=current_user_id)

    if not current_user in likes:
        print('adding like...')
        quote.likes.add(current_user)
    
    return redirect('/quotes')

def user(request, id):
    user = User.objects.get(id=id)
    quotes = Quotes.objects.filter(user=user)
    context = {
        'quotes': quotes,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'currentid': user.id

    }
    return render(request, 'user.html', context)

def myaccount(request, id):
    user = User.objects.get(id=id)
    
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'id': user.id
    }

    return render(request, 'myaccount.html', context)


def update(request, id):
    user = User.objects.get(id=id)
    errors = User.objects.edit_validator(request.POST)

    isRegistered = len(User.objects.filter(email=request.POST['email']).all()) > 0

    if len(errors) > 0 and user:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
    
    return redirect('/myaccount/' + str(id))
