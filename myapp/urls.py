from django.contrib import admin
from django.urls import path,include
from. import views
from myapp.routes import router

urlpatterns = [
 
    path('office/',include(router.urls))
]
