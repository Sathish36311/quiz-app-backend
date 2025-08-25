from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]