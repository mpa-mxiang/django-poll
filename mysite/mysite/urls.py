"""
URL configuration for your Django project.

This module defines the URL patterns for your project, including paths
for the admin interface and the 'polls' app.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
