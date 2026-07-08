from django.shortcuts import render
from rest_framework import viewsets
from data.models import Fac
from api.serializers import FacSerializers
# Create your views here.
class facviewset(viewsets.ModelViewSet):
    queryset=Fac.objects.all
    serializer_class=FacSerializers