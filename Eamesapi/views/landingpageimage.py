from django.http import FileResponse
from django.http import HttpResponse
from django.conf import settings
import os


def serve_landing_page_image():
    image_path = os.path.join(settings.MEDIA_ROOT, 'landing_page', 'eames-overlook.jpeg')
    if os.path.exists(image_path):
        return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
    else:
        return HttpResponse("Image not found", status=404)