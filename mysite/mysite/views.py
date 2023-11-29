from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')