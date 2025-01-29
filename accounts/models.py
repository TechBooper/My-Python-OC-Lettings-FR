from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile with additional information.

    Attributes:
        user (OneToOneField): A one-to-one relationship to the Django User model.
        favorite_city (CharField): The user's favorite city, optional and up to 64 characters.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns the username of the associated user as the string representation.

        Example:
            'johndoe'
        """
        return self.user.username
