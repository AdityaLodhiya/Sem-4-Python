from django.db import models


class Player(models.Model):
    name=models.CharField(max_length=50)
    team=models.CharFiels()
    score=models.IntegerField()
    email=models.EmailField( max_length=254)
    birthdate=models.DateField(auto_now=False)