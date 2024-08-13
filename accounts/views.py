from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .models import User

from .serializers import UserRegistrationSerializer

# Create your views here.


class RegisterUserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer