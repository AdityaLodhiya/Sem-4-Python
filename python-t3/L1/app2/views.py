from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def python(request):
    return render(request,"python.html")