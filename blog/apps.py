"""
The configuration for the blog application.

This module contains the configuration for the blog application. The
configuration is used by Django to load the application.

"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    The configuration for the blog application.

    This class is used to configure the application. It is used by Django
    to load the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
