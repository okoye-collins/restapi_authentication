from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from .models import OneTimePassword, User

from .serializers import UserRegistrationSerializer, VerifyUserEmailSerializer

# Create your views here.


class RegisterUserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class VerifyUserEmailViewSet(viewsets.ModelViewSet):
    
    queryset = OneTimePassword.objects.all()
    serializer_class = VerifyUserEmailSerializer
    
    # @action(detail=True, methods=['POST'], permission_classes=[AllowAny])
    # def verify(self, request):
    #     otp_code = request.data
        
    #     print('============', otp_code)
    #     return Response("ok")