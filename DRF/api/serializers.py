from rest_framework import serializers
from api.models import Student,Faculty

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        #fields=['id','name','roll','mark']
        fields='__all__'
    
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields='__all__'