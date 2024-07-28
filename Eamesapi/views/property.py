from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Eamesapi.models import Property
from rest_framework import permissions

class PropertySerializer(serializers.ModelSerializer):
    """JSON serializer for properties"""

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
        )

class PropertiesViewSet(ViewSet):
    """Request handlers for properties"""

    # permission_classes = (permissions.AllowAny)

    def list(self, request):

        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True, context={'request': request})
        return Response(serializer.data)