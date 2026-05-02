from django.shortcuts import render
from rest_framework import generics

from .models import Entities, Tags, TagsOfEntities, Interpretations, InterpretationOfEntities
from .serializers import EntitiesSerializer, TaggingSerializer, TaggingEntitiesSerializer, InterpretSerializer, InterpretEntitiesSerializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# Create your views here.
class SoulsEntityList(generics.ListCreateAPIView):
    queryset = Entities.objects.all()
    serializer_class = EntitiesSerializer


class TaggingList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TaggingSerializer

class TagsOfEntsList(generics.ListCreateAPIView):
    queryset = TagsOfEntities.objects.all()
    serializer_class = TaggingEntitiesSerializer


class InterpretList(generics.ListCreateAPIView):
    queryset = Interpretations.objects.all()
    serializer_class = InterpretSerializer
    
class InterpretEntsList(generics.ListCreateAPIView):
    queryset = InterpretationOfEntities.objects.all()
    serializer_class = InterpretEntitiesSerializer


#     @api_view(['POST'])
#     def postTag(request):
#         entity_id = request.data.get('entity_id')
#         tag_name = request.data.get('tag_name').lower()
        
#         tag, created = Tags.objects.get_or_create(name=tag_name)
#         entity = Entities.objects.get(id="entity_id")
#         EntityTags.objects.create(entity=entity, tag=tag)
        
#         return Response({"message": "ENTITY TAGGED"}, status=201)
    

#     @api_view(['POST'])
#     def postInterpretation(request):
#         entity_id = request.data.get('entity_id')
#         body = request.data.get('body')
        
#         interpretation = Interpretations.objects.create(body=body)
#         entity = Entities.objects.get(id=entity_id)
        
#         InterpretationEntities.objects.create(
#             interpretation=interpretation,
#             entity=entity
#         )
        
#         return Response({"message": "THEORY CRAFTED"}, status=201)