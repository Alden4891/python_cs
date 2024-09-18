# Django Cheat Sheet

# ------------------------------
# 1. Installation and Setup
# ------------------------------

# Install Django:
# Comment: Install Django from PyPI.
# Syntax: pip install django
pip install django

# Create a New Django Project:
# Comment: Create a new Django project called "myproject".
# Syntax: django-admin startproject project_name
django-admin startproject myproject

# Create a New Django App:
# Comment: Create a new Django app within the project.
# Syntax: python manage.py startapp app_name
python manage.py startapp myapp

# Run the Development Server:
# Comment: Start the development server on http://127.0.0.1:8000.
# Syntax: python manage.py runserver
python manage.py runserver

# ------------------------------
# 2. Django Project Structure
# ------------------------------
"""
myproject/
    manage.py          # Command-line utility for Django
    myproject/
        __init__.py    # Marks the directory as a Python package
        settings.py    # Project settings
        urls.py        # URL configuration
        asgi.py        # ASGI config for asynchronous support
        wsgi.py        # WSGI config for deployment
    myapp/             # Django app
        migrations/    # Database migrations
        models.py      # Database models
        views.py       # Request/response logic
        urls.py        # App-specific URLs
        templates/     # HTML templates
"""

# ------------------------------
# 3. Django Models
# ------------------------------

# Create a Model:
# Comment: Define a model representing a database table.
# Syntax: class ModelName(models.Model)
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Run Migrations:
# Comment: Create and apply migrations for the database schema.
# Syntax: python manage.py makemigrations; python manage.py migrate
python manage.py makemigrations
python manage.py migrate

# Model Methods:
# Comment: Add methods to interact with data or represent it.
def __str__(self):
    return self.name

# ------------------------------
# 4. Django Admin
# ------------------------------

# Register Models in Admin:
# Comment: Register your model in the Django admin site to manage it.
# Syntax: admin.site.register(ModelName)
from django.contrib import admin
from .models import Product

admin.site.register(Product)

# Access Django Admin:
# URL: http://127.0.0.1:8000/admin/

# Create Superuser:
# Comment: Create a superuser with full access to the Django admin.
# Syntax: python manage.py createsuperuser
python manage.py createsuperuser

# ------------------------------
# 5. Django Views
# ------------------------------

# Basic View:
# Comment: Define a view to handle a request and return a response.
# Syntax: def view_name(request)
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")

# Render a Template:
# Comment: Render an HTML template in a view.
# Syntax: render(request, "template.html", context)
from django.shortcuts import render

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product_detail.html", {"product": product})

# Redirect to Another URL:
# Comment: Redirect to another view or URL.
# Syntax: redirect("url_name")
from django.shortcuts import redirect

def product_redirect(request):
    return redirect("product_list")

# ------------------------------
# 6. Django URL Routing
# ------------------------------

# Project-level URL Configuration:
# Comment: Define URL patterns for the project.
# Syntax: path("route/", view_function)
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/<int:product_id>/", views.product_detail, name="product_detail"),
]

# App-level URL Configuration:
# Comment: Include app-specific URLs in the project.
# Syntax: path("route/", include("app.urls"))
from django.urls import include

urlpatterns = [
    path("app/", include("myapp.urls")),
]

# ------------------------------
# 7. Django Templates
# ------------------------------

# Basic Template Syntax:
# Comment: Django templates use curly braces for variables and logic.
# Syntax: {{ variable }} and {% tag %}
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
</body>
</html>
"""

# Template Inheritance:
# Comment: Use template inheritance to reuse common layouts.
"""
# base.html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Site</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>

# child_template.html
{% extends "base.html" %}
{% block title %}Product Details{% endblock %}
{% block content %}
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
{% endblock %}
"""

# ------------------------------
# 8. Django Forms
# ------------------------------

# Creating a Form:
# Comment: Define a form for user input.
# Syntax: class FormName(forms.Form)
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea)

# Using a Form in a View:
# Comment: Process form data in a view and handle validation.
from django.shortcuts import render

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process form data
            pass
    else:
        form = ProductForm()
    return render(request, "product_create.html", {"form": form})

# Template for Displaying Form:
# Comment: Render a form in an HTML template.
"""
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
"""

# ------------------------------
# 9. Django ORM Queries
# ------------------------------

# Basic ORM Queries:
# Comment: Use Django's ORM to query the database.
# Syntax: Model.objects.all(), Model.objects.get(), etc.

# Get All Objects:
products = Product.objects.all()

# Get a Single Object:
product = Product.objects.get(id=1)

# Filter Objects:
cheap_products = Product.objects.filter(price__lt=500)

# Order By:
ordered_products = Product.objects.order_by("-price")

# Create a New Object:
new_product = Product.objects.create(name="New Product", price=99.99, description="A new product")

# ------------------------------
# 10. Django Middleware
# ------------------------------

# Custom Middleware:
# Comment: Create custom middleware for processing requests or responses.
# Syntax: class MiddlewareName
from django.utils.deprecation import MiddlewareMixin

class MyCustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Request received")

    def process_response(self, request, response):
        print("Response sent")
        return response

# Add Middleware to Settings:
# Comment: Register custom middleware in the Django settings.
# Syntax: MIDDLEWARE = ["path.to.middleware"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "myproject.middleware.MyCustomMiddleware",
]

# ------------------------------
# 11. Static Files and Media Files
# ------------------------------

# Static Files:
# Comment: Manage CSS, JavaScript, and other static files.
# Settings:
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media Files:
# Comment: Manage uploaded files.
# Settings:
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------
# 12. Django Settings Customization
# ------------------------------

# Update Settings:
# Comment: Configure various aspects of your Django project.
# Example: Setting DEBUG, database, and installed apps.
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",  # Your app
]

# ------------------------------
# 13. Django User Authentication
# ------------------------------

# User Registration Form:
# Comment: Use Django’s built-in user authentication system.
from django.contrib.auth.forms import UserCreationForm

# View for User Registration:
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# URLs for Login and Logout:
# Comment: Use Django’s built-in authentication views.
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name
