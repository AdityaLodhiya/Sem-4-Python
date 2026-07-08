from django.shortcuts import render,get_object_or_404,redirect
from student.models import Python
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    data=Python.objects.all()
    return render(request,'home.html',{'data':data})

def info(request,id):
    marks=get_object_or_404(Python,id=id)
    return render(request,'info.html',{'m':marks})


def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        score=request.POST['score']
        sub=request.POST['sub']
        Python.objects.create(name=name,score=score,sub=sub)
        return redirect('home')
    return render(request,'form.html')

@login_required
def edit(request,id):
    stu=get_object_or_404(Python,id=id)
    if request.method == 'POST':
        stu.name=request.POST['name']
        stu.score=request.POST['score']
        stu.sub=request.POST['sub']
        stu.save()
        return redirect('home')
    return render(request,'edit.html',{'stu':stu})

@login_required
def delete_obj(request,id):
    stu=get_object_or_404(Python,id=id)
    stu.delete()
    return redirect('home')