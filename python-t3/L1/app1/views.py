from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello Page</h1><a href='/welcome'>welcome page<a><br><a href='/python'>Python page<a><br><a href='/app3'>welcome page<a>")

def welcome(request):
    return HttpResponse("<h1>2nd Page</h1><a href='/'>Home page<a><br><a href='/python'>Python page<a><br><a href='/app3'>welcome page<a>")