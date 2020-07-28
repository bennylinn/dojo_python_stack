from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse

def index(request):
    session_function(request)
    context = {
        'count': request.session['count']
    }
    return render(request, 'index.html', context)

# def create_user(request):
#     print('>>>>>>>> GETTING POST DATA...............')
#     session_function(request)
#     return redirect('/success')

# def success(request):
#     context = {
#         'name_on_template': request.session['name'],
#         'email_on_template': request.session['email'],
#         'favNums_on_template': request.session['favNums']
#     }
#     return render(request, 'show.html', context)




# def session_function(request):
#     request.session['name'] = request.POST['name']
#     request.session['email'] = request.POST['email']
#     request.session['favNums'] = [request.POST['favNumber1'], request.POST['favNumber2'], request.POST['favNumber3']]


def session_function(request):
    if 'count' in request.session:
        print('counter exists!')
        print('incrementing.....')
        request.session['count'] = request.session['count'] + 1
    else:
        print('counter does not exist')
        request.session['count'] = 1

def delete(request):
    try:
        del request.session['count']
    except KeyError:
        print('No count key saved on session.')
    return redirect('/')