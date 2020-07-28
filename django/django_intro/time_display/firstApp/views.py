from django.shortcuts import render

# Create your views here.
def time_display(request):
    return render(request, 'time_display.html')