from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from Eamesapi.models import Property, PropertyType, Amenity
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
import base64
import re


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""

    class Meta:
        model = User
        fields = ('id', 'username')

class AmenitySerializer(serializers.ModelSerializer):
    """JSON serializer for amenities"""

    class Meta:
        model = Amenity
        fields = ('id', 'name')

class PropertyTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for property type"""

    class Meta:
        model = PropertyType
        fields = ('id', 'name')

class PropertySerializer(serializers.ModelSerializer):
    """JSON serializer for properties"""

    property_type = PropertyTypeSerializer()
    amenities = AmenitySerializer(many=True)
    owner = UserSerializer(read_only=True)

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
            "amenities",
        )
        extra_kwargs = {
            'owner': {'read_only': True}, # Owner is read only (determined by logged in user that creates property)
        }


class PropertyViewSet(ViewSet):
    """Request handlers for properties"""

    permission_classes = [IsAuthenticated] # Ensure the user is authenticated

    def list(self, request):

        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True, context={'request': request})
        return Response(serializer.data)
    
    def list_by_owner(self, request):
        """Handle GET requests for listing properties by owner (auth token in header)"""

        owner = request.user
        properties = Property.objects.filter(owner=owner)
        serializer = PropertySerializer(properties, many=True, context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests for creating a new property"""

        # create a mutable copy of the request data
        # allows modification to request data to meet needs without affecting original request data
        # ensures owner field can be set to the logged in user
        data = request.data.copy()
        data['owner'] = request.user.id

        # ensure the image is present
        if "image" not in data:
            return Response({"error": "Image is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        new_property = Property()
        new_property.name = data["name"]
        new_property.description = data["description"]
        new_property.price_per_night = data["price_per_night"]
        new_property.cleaning_fee = data["cleaning_fee"]
        # new_property.address = data["address"]
        new_property.city = data["city"]
        new_property.state = data["state"]
        new_property.max_guests = data["max_guests"]
        new_property.bedrooms = data["bedrooms"]
        new_property.bathrooms = data["bathrooms"]

        owner = User.objects.get(pk=data["owner"])
        new_property.owner = owner

        property_type = PropertyType.objects.get(pk=data["property_type"]["id"])
        new_property.property_type = property_type

        # Handle image upload
        format, imgstr = data["image"].split(";base64,") # Split the base64 string
        ext = format.split("/")[-1] # Extract the file extension

        # Convert property name to kebab case for image file name
        kebab_case_name = re.sub(r'\s+', '-', data["name"].lower())

        image_data = ContentFile(
            base64.b64decode(imgstr), # Decode the base64 string
            name=f'{kebab_case_name}.{ext}', # Set the file name
        )
        new_property.image = image_data # Assign the image to the property

        new_property.save()

        # Handle amenities
        if "amenities" in data:
            amenities = data["amenities"]
            for amenity_data in amenities:
                amenity = Amenity.objects.get(pk=amenity_data["id"])
                new_property.amenities.add(amenity)

        serializer = PropertySerializer(new_property, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)