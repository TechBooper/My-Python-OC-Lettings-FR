from django.apps import AppConfig


class PropertyLettingsConfig(AppConfig):
    """
    Configuration class for the 'property_lettings' app.

    Attributes:
        default_auto_field (str): Specifies the default type of auto-generated primary key field.
        name (str): The name of the application ('property_lettings').
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "property_lettings"
