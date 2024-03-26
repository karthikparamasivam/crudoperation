from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from myapp.models import Office
from myapp.serializers import Officeserializer

class Growth(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = Officeserializer