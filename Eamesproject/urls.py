from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from Eamesapi.views import *
from Eamesapi.models import *
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'properties', PropertyViewSet, 'property')
router.register(r'amenities', AmenityViewSet, 'amenity')
router.register(r'property-types', PropertyTypeViewSet, 'property-type')

urlpatterns = [
    path('', include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("api-token-auth", obtain_auth_token),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
    path('landing-page-image/', serve_landing_page_image, name='landing_page_image'),
    path('properties/by-owner', PropertyViewSet.as_view({'get': 'list_by_owner'}), name='properties-by-owner'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)