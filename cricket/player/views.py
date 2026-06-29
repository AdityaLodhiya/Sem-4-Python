from django.shortcuts import render,get_object_or_404
from player.models import Players
# Create your views here.

def home(request):
    p=Players.objects.all().order_by('runs')
    return render(request,'home.html',{'p':p})

def about(request):
    return render(request,'about.html')

def info(request,id):
    play = get_object_or_404(Players,id=id)
    return render(request,'info.html',{"play":play})
