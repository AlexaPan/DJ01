from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Test Index Page </h1>")

def new(request):
    return HttpResponse("<h1> Test New Page </h1>")

def homework_first(request):
    return HttpResponse("<h1> Test Homework First Page </h1>")

def homework_second(request):
    return HttpResponse("<h1> Test Homework Second Page </h1>")

