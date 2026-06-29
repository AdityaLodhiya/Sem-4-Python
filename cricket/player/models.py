from django.db import models

# Create your models here.

class Players(models.Model):
    name=models.CharField(max_length=50)
    runs=models.IntegerField()
    profile=models.URLField(max_length=100)
    email=models.EmailField(max_length=100)
    dob=models.DateField(blank=True)
    
    def __str__(self):
        return self.name