from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
#CRUD OPERATION

class ListClient(generics.ListAPIView):       #read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailClient(generics.RetrieveUpdateAPIView):       #update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class CreateClient(generics.CreateAPIView):       #create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DeleteClient(generics.DestroyAPIView):      #delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer