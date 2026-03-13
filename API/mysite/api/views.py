from django.shortcuts import render
from rest_framework import generics
from .models import Soulsborne
from .serializers import SoulsborneSerializer

# Create your views here.
class SoulsborneListCreate(generics.ListCreateAPIView):
    queryset = Soulsborne.objects.all()
    serializer_class = SoulsborneSerializer