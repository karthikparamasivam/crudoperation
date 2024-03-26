from django.contrib import admin
from django.urls import path,include
from. import views
from app.routes import router

urlpatterns = [
    path('index/', views.home, name='home'),
    path('student/',include(router.urls))
]
