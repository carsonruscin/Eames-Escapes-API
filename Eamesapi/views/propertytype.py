from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from Eamesapi.models import PropertyType


class PropertyTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for property types"""

    class Meta:
        model = PropertyType
        fields = ('id', 'name')

class PropertyTypeViewSet(ViewSet):
    """Request handlers for property types"""

    def list(self, request):

        property_types = PropertyType.objects.all()
        serializer = PropertyTypeSerializer(property_types, many=True, context={'request': request})
        return Response(serializer.data)