import logging
from django.conf import settings
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Eamesapi.models import LandingPageImage

logger = logging.getLogger(__name__)

class LandingPageImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = LandingPageImage
        fields = ['id', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            url = self.context['request'].build_absolute_uri(obj.image.url)
            return url.rstrip('/')  # Remove trailing slash if present
        return None

class LandingPageImageViewSet(viewsets.ModelViewSet):
    queryset = LandingPageImage.objects.all()
    serializer_class = LandingPageImageSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        logger.info(f"Received request for landing page image. Path: {request.path}")
        image = self.get_queryset().first()
        if image:
            serializer = self.get_serializer(image, context={'request': request})
            data = serializer.data
            logger.info(f"Returning image URL: {data.get('image_url')}")
            return Response(data)
        logger.warning("No landing page image found")
        return Response({'image_url': None})