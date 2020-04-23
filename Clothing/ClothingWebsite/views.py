from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.


def Homepage(request):
    return render(request, 'basic.html')