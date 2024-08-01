from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Eamesapi.models import Property
from rest_framework import permissions
from Eamesapi.models import PropertyType


class PropertyTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for property type"""

    class Meta:
        model = PropertyType
        fields = ('id', 'name')

class PropertySerializer(serializers.ModelSerializer):
    """JSON serializer for properties"""

    property_type = PropertyTypeSerializer(read_only=True)

    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "owner",
            "property_type",
            "description",
            "price_per_night",
            "cleaning_fee",
            "address",
            "city",
            "state",
            "max_guests",
            "bedrooms",
            "bathrooms",
            "image",
        )


class PropertiesViewSet(ViewSet):
    """Request handlers for properties"""


    def list(self, request):

        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True, context={'request': request})
        return Response(serializer.data)