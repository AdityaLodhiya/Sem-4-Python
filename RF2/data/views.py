from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from data.models import Fac
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    fac=Fac.objects.all()
    return render(request,'home.html',{'fac':fac})

def add(request):
    if request.method=="POST":
        name=request.POST['name']
        subject=request.POST['subject']
        score=request.POST['score']
        grade=request.POST['grade']
        pr_grade=request.POST['name']
        Fac.objects.create(name=name,subject=subject,score=score,grade=grade,pr_grade=pr_grade)
        return redirect('home')
    return render(request,'add.html')

def edit(request,name):
    fac=get_object_or_404(Fac,name=name)
    if request.method=="POST":
        fac.name=request.POST['name']
        fac.subject=request.POST['subject']
        fac.score=request.POST['score']
        fac.grade=request.POST['grade']
        fac.pr_grade=request.POST['name']
        fac.save()
        return redirect('home')
    return render(request,'edit.html')

def delete(request,name):
    fac=get_object_or_404(Fac,name)
    fac.delete()
    return redirect('home')