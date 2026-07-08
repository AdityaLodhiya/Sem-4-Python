from rest_framework import serializers
from data.models import  Fac
class FacSerializers(serializers.ModelSerializer):
    class Meta:
        model=Fac
        fields='__all__'