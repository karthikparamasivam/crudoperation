from rest_framework import serializers
from myapp.models import Office

class Officeserializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['name','age','email','qualification','dob']