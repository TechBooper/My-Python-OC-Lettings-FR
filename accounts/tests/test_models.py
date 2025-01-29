from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile


class ProfileModelTestCase(TestCase):
    """
    Test suite for the Profile model.
    """

    def setUp(self):
        """
        Set up test users and profiles for use in tests.
        """
        # Create test users
        self.user1 = User.objects.create_user(
            username="testuser1", password="password123"
        )
        self.profile1 = Profile.objects.create(user=self.user1, favorite_city="Paris")

        self.user2 = User.objects.create_user(
            username="testuser2", password="password123"
        )
        self.profile2 = Profile.objects.create(
            user=self.user2, favorite_city="New York"
        )

    # Unit Tests
    def test_profile_creation(self):
        """
        Test that Profile instances are created with the correct attribute values.
        """
        self.assertEqual(self.profile1.user.username, "testuser1")
        self.assertEqual(self.profile1.favorite_city, "Paris")

        self.assertEqual(self.profile2.user.username, "testuser2")
        self.assertEqual(self.profile2.favorite_city, "New York")

    def test_profile_string_representation(self):
        """
        Test the string representation of Profile instances.
        """
        self.assertEqual(str(self.profile1), "testuser1")
        self.assertEqual(str(self.profile2), "testuser2")

    def test_profile_optional_favorite_city(self):
        """
        Test that the favorite_city field is optional.
        """
        user3 = User.objects.create_user(username="testuser3", password="password123")
        profile3 = Profile.objects.create(user=user3)  # No favorite_city provided
        self.assertEqual(profile3.favorite_city, "")  # Default blank value

    # Integration Tests
    def test_profile_user_relationship(self):
        """
        Test the one-to-one relationship between User and Profile.
        """
        self.assertEqual(self.profile1.user.profile, self.profile1)
        self.assertEqual(self.profile2.user.profile, self.profile2)

    def test_profile_deletion_cascade(self):
        """
        Test that deleting a User also deletes the associated Profile.
        """
        self.user1.delete()
        with self.assertRaises(Profile.DoesNotExist):
            Profile.objects.get(user=self.user1)
