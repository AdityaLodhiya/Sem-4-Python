from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import Player
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PlayerSerializer
# Create your views here.
@api_view(['GET','POST'])
def Api_demo(request):
    if request.method=='GET':
        p=Player.objects.all()
        serializer=PlayerSerializer(p,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.Error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def Api_detail(request,id):
    try:
        p=Player.objects.get(id=id)
    except:
        return Response({'message':'record not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=PlayerSerializer(p)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.Error,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        p.delete()
        return Response({'message':'Bye Bye'},status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PATCH':
        serializer=PlayerSerializer(p,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)