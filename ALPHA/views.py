from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Bem-vindo ao site da ALPHA!")
