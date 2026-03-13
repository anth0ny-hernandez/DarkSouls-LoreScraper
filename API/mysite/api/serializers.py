from rest_framework import serializers
from .models import Soulsborne

class SoulsborneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soulsborne
        fields = [
            "url",
            "item_icon",
            "item_name",
            "item_use",
            "item_availability",
            "item_description",
            "category_type"
        ]