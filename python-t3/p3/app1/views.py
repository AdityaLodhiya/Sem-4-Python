from django.shortcuts import render

# Create your views here.
def home(request):
    l=[1,2,3]
    return render(request,'home.html',{'data':l})
def about(request):
    return render(request,'about.html')