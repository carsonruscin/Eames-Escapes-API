from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from Eamesapi.models import Amenity


class AmenitySerializer(serializers.ModelSerializer):
    """JSON serializer for amenities"""

    class Meta:
        model = Amenity
        fields = ('id', 'name')

class AmenityViewSet(ViewSet):
    """Request handlers for amenities"""

    def list(self, request):

        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True, context={'request': request})
        return Response(serializer.data)