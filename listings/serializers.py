from rest_framework import serializers
from .models import Estate

class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'

    def validate(self, data):
        # check karne ke phele se same title and property type ka property exist to nahin karta.
        existing_property = Estate.objects.filter(title=data['title'], property_type=data['property_type']).first()
        if existing_property:
            raise serializers.ValidationError("A property with the same title and property type already exists.")
        return data