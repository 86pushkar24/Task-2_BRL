from rest_framework import serializers
from .models import Estate

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'

    def validate(self, data):
        # check karne ke phele se same title and property type ka property exist to nahin karta.
        existing = Estate.objects.filter(title=data['title'], property_type=data['property_type']).first()
        if existing:
            raise serializers.ValidationError("Bhai Nayin Property daal!!")
        return data
    