from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address associated with a letting.

    Attributes:
        number (PositiveIntegerField): The street number, limited to 4 digits.
        street (CharField): The name of the street, with a maximum length of 64 characters.
        city (CharField): The city name, with a maximum length of 64 characters.
        state (CharField): The 2-character state code (e.g., 'CA', 'NY'), validated for minimum length.
        zip_code (PositiveIntegerField): The 5-digit ZIP code.
        country_iso_code (CharField): The 3-character ISO code for the country (e.g., 'USA').
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Returns a string representation of the address.

        Format:
            '<number> <street>'
        Example:
            '123 Main Street'
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a letting, which links to a specific address.

    Attributes:
        title (CharField): The title or name of the letting.
        address (OneToOneField): A one-to-one relationship to an Address instance.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the title of the letting as its string representation.

        Example:
            'Beautiful Apartment in Paris'
        """
        return self.title
