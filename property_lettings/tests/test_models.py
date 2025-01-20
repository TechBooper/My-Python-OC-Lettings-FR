import unittest
from property_lettings.models import Address, Letting
from django.test import TestCase
import os
import django

# Set up the Django environment for testing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()


class TestAddressModel(TestCase):
    """
    Test suite for the Address model.
    """

    def setUp(self):
        """
        Set up a test Address instance for use in tests.
        """
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Springfield",
            state="IL",
            zip_code=62704,
            country_iso_code="USA",
        )

    def test_address_creation(self):
        """
        Test that an Address instance is created with correct attribute values.
        """
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, "Main Street")
        self.assertEqual(self.address.city, "Springfield")
        self.assertEqual(self.address.state, "IL")
        self.assertEqual(self.address.zip_code, 62704)
        self.assertEqual(self.address.country_iso_code, "USA")

    def test_address_string_representation(self):
        """
        Test the string representation of an Address instance.
        """
        self.assertEqual(str(self.address), "123 Main Street")

    def test_verbose_name_plural(self):
        """
        Test that the plural verbose name of the Address model is 'Addresses'.
        """
        self.assertEqual(Address._meta.verbose_name_plural, "Addresses")


class TestLettingModel(TestCase):
    """
    Test suite for the Letting model.
    """

    def setUp(self):
        """
        Set up a test Letting instance and associated Address instance for use in tests.
        """
        self.address = Address.objects.create(
            number=456,
            street="Elm Street",
            city="Hometown",
            state="CA",
            zip_code=90210,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Charming Bungalow",
            address=self.address,
        )

    def test_letting_creation(self):
        """
        Test that a Letting instance is created with correct attribute values.
        """
        self.assertEqual(self.letting.title, "Charming Bungalow")
        self.assertEqual(self.letting.address, self.address)

    def test_letting_string_representation(self):
        """
        Test the string representation of a Letting instance.
        """
        self.assertEqual(str(self.letting), "Charming Bungalow")


if __name__ == "__main__":
    unittest.main()
