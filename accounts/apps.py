"""
This module defines the AppConfig for the 'accounts' application.

It specifies:
- The default primary key field type for the app's models.
- The name of the application as 'accounts'.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the 'accounts' application.

    Attributes:
        default_auto_field (str): Specifies the type of primary key field to use
            for models in this app (BigAutoField).
        name (str): The official name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
