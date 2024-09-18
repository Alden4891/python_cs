# Django RESTful API Cheat Sheet

# ------------------------------
# 1. Installation
# ------------------------------

# Install Django and Django REST Framework:
# Comment: Install Django and DRF using pip.
# Syntax: pip install django djangorestframework
pip install django djangorestframework

# ------------------------------
# 2. Project Setup
# ------------------------------

# Create a New Django Project:
# Comment: Create a new Django project.
# Syntax: django-admin startproject project_name
django-admin startproject myproject

# Navigate to Project Directory:
# Comment: Change directory to the project folder.
cd myproject

# Create a New Django App:
# Comment: Create a new app within the Django project.
# Syntax: python manage.py startapp app_name
python manage.py startapp myapp

# ------------------------------
# 3. Configure Django REST Framework
# ------------------------------

# Add DRF to Installed Apps:
# Comment: Add 'rest_framework' to the `INSTALLED_APPS` list in settings.py.
# Syntax: INSTALLED_APPS = ['rest_framework', ...]
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'myapp',
]

# Set Up Default Permissions:
# Comment: Configure default permissions in settings.py.
# Syntax: REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny']}
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# ------------------------------
# 4. Create Models
# ------------------------------

# Define a Model:
# Comment: Create a model in myapp/models.py.
# Syntax: Use Django's model class to define the schema.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# ------------------------------
# 5. Create Serializers
# ------------------------------

# Create a Serializer:
# Comment: Create a serializer to convert model instances to JSON.
# Syntax: Use serializers.ModelSerializer to define serialization.
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price']

# ------------------------------
# 6. Create Views
# ------------------------------

# Create API Views:
# Comment: Define views to handle API requests.
# Syntax: Use viewsets.ModelViewSet for CRUD operations.
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# ------------------------------
# 7. Define URL Routes
# ------------------------------

# Set Up URL Routing:
# Comment: Create URL routes for API endpoints.
# Syntax: Use routers.DefaultRouter to register viewsets.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# ------------------------------
# 8. Run Migrations
# ------------------------------

# Make Migrations:
# Comment: Create migration files for the changes in models.
# Syntax: python manage.py makemigrations
python manage.py makemigrations

# Apply Migrations:
# Comment: Apply the migrations to the database.
# Syntax: python manage.py migrate
python manage.py migrate

# ------------------------------
# 9. Testing API Endpoints
# ------------------------------

# Run the Development Server:
# Comment: Start the Django development server to test the API.
# Syntax: python manage.py runserver
python manage.py runserver

# Access API Endpoints:
# Comment: Access the API through the browser or tools like Postman.
# Example: http://127.0.0.1:8000/items/

# ------------------------------
# 10. Authentication and Permissions
# ------------------------------

# Basic Authentication:
# Comment: Use basic authentication in settings.py.
# Syntax: 'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.BasicAuthentication']
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
}

# Token Authentication:
# Comment: Use token-based authentication.
# Syntax: pip install djangorestframework-simplejwt
pip install djangorestframework-simplejwt

# Update settings.py for JWT Authentication:
# Syntax: 'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication']
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Configure JWT:
# Comment: Add JWT settings in settings.py.
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# ------------------------------
# 11. API Documentation
# ------------------------------

# Install DRF-YASG for Swagger Documentation:
# Comment: Install DRF-YASG for API documentation.
# Syntax: pip install drf-yasg
pip install drf-yasg

# Add Swagger Documentation to URLs:
# Comment: Update urls.py to include Swagger documentation.
from rest_framework_yasg import openapi
from rest_framework_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
]
