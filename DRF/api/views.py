from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import Student,Faculty
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import StudentSerializer,FacultySerializer
# Create your views here.

@api_view(['GET','POST'])
def Home(request):
    if request.method=="GET":
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        student=Student.objects.all()
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def Home2(request):
    fac=Faculty.objects.all()
    serializer=FacultySerializer(fac,many=True)
    return Response(serializer.data)
    








# def Home(request):
#     s=Student.objects.all()
#     j=list(s.values())
#     d={"id":1,'name':'Adi','grade':10}
#     return JsonResponse(j,safe=False)
    
    