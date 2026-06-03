from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hii(request):
    return render(request,"app3.html")