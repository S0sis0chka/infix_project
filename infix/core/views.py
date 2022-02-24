from django.shortcuts import render
from .utils import *

def homepage(request):
    return render(request, 'homepage.html')

def calculate(request):
    if request.method == 'POST':
        from_v = request.POST['from']
        to_v = request.POST['to']
        text = request.POST['text']
        res = calc(from_v, to_v, text)
        return render(request, 'calculate.html', {'result': res})
    else:
        return render(request, 'calculate.html')