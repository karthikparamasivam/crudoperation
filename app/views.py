from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from app.models import Student
from app.serializers import Studentserializer

def home(request):
    return render(request,'home.html'),

class Journey(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

