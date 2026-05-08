from django.shortcuts import render
from rest_framework import generics

from .models import Entities, Tags, TagsOfEntities, Interpretations, InterpretationOfEntities
from .serializers import EntitiesSerializer, TaggingSerializer, TaggingEntitiesSerializer, InterpretSerializer, InterpretEntitiesSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SoulsEntityList(generics.ListCreateAPIView):
    queryset = Entities.objects.all()
    serializer_class = EntitiesSerializer


class TaggingList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TaggingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

class TagsOfEntsList(generics.ListCreateAPIView):
    queryset = TagsOfEntities.objects.all()
    serializer_class = TaggingEntitiesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['entity']


class InterpretList(generics.ListCreateAPIView):
    queryset = Interpretations.objects.all()
    serializer_class = InterpretSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    
class InterpretEntsList(generics.ListCreateAPIView):
    queryset = InterpretationOfEntities.objects.all()
    serializer_class = InterpretEntitiesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['entity']
