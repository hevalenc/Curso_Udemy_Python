from django.urls import path
from . import views #o '.' referencia a própria pasta do arquivo

urlpatterns = [
    path('', views.index),
]