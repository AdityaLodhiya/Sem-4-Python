from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    marks=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    fb=models.CharField(max_length=50)
    rating=models.IntegerField()
    
    def __str__(self):
        return self.fb