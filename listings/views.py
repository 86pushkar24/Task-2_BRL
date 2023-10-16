from rest_framework import generics
from .models import Estate
from .serializers import ListingSerializer

# for listing all the properties and creating a new property.
class listcreate(generics.ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        # validator for checking price is positive.
        if serializer.validated_data['price'] < 0:
            raise serializer.ValidationError("Price cannot be negative.")
        serializer.save()

# for updating, retrieving and deleting a property.(postman se ho raha hain// how to do it from browser?)
class updateretreivedestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estate.objects.all()
    serializer_class = ListingSerializer

# for filtering by property type.
class filterproperty(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        property_type = self.request.query_params.get('property_type', '')
        return Estate.objects.filter(property_type=property_type)

class filterbedroom(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        bedrooms = self.request.query_params.get('bedrooms', 0)
        return Estate.objects.filter(bedrooms__gt=bedrooms)

# for cheap property filtering.
class cheap(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        n = self.request.query_params.get('n', 10)
        return Estate.objects.order_by('price')[:n]




