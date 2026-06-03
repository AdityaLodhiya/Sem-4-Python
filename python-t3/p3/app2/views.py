from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact.html')
def base(request):
    name='aditya'
    number=10
    return render(request,'base.html',{'n':name,'fb':number})