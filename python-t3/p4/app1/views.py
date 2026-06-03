from django.shortcuts import render
from app1.models import Student

# Create your views here.
def home(request):
    search_term=request.GET.get('search')
    search_term2=request.GET.get('search_roll')
    if search_term:
        stu=Student.objects.filter(name__icontains=search_term)
    else:
        stu=Student.objects.all()
        
        
    if search_term2:
        stu=Student.objects.filter(roll__icontains=search_term2)
    else:
        stu=Student.objects.all().order_by('mark')
    return render(request,'home.html',{'stu':stu})

def det(request,student_id):
    st=Student.objects.get(pk=student_id)
    return render(request,'det.html',{'st':st}) 