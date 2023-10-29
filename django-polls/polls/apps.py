"""
Django AppConfig for the Polls app.

This module defines the AppConfig for the Polls app, including the
app's name and the default_auto_field configuration.
"""

from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    AppConfig for the Polls app.

    This class defines the configuration for the Polls app, including the
    app's name and the default_auto_field setting.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
