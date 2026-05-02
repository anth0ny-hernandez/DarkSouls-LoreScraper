from rest_framework import serializers
from .models import Entities, References, Tags, TagsOfEntities, Interpretations, InterpretationOfEntities

class EntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entities
        db_table = 'entities'
        fields = [
            "id",
            "url",
            "item_icon",
            "item_name",
            "item_use",
            "item_availability",
            "item_description",
            "category_type"
        ]
        
        
class TaggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        db_table = 'tags'
        fields = ["id", "tag"]
        
class TaggingEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsOfEntities
        db_table = 'tag_entity'
        fields = ["id", "entity", "tag"]
        

class InterpretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpretations
        db_table = 'interpretations'
        fields = ["id", "comments"]

class InterpretEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterpretationOfEntities
        db_table = 'interpret_entities'
        fields = ["id", "entity", "interpret"]