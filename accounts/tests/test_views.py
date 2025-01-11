from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Profile
from django.urls import reverse

class AccountsViewsTestCase(TestCase):
    """
    Test suite for the views in the /accounts app.
    """

    def setUp(self):
        """
        Set up test users and profiles for use in tests.
        """
        # Create test users and profiles
        self.user1 = User.objects.create_user(username="testuser1", password="password123")
        self.profile1 = Profile.objects.create(user=self.user1, favorite_city="Paris")

        self.user2 = User.objects.create_user(username="testuser2", password="password123")
        self.profile2 = Profile.objects.create(user=self.user2, favorite_city="New York")

        # Set up the test client
        self.client = Client()

    # Unit Tests
    def test_index_renders_correct_template(self):
        """
        Test that the index view renders the correct template.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profile_view_renders_correct_template(self):
        """
        Test that the profile view renders the correct template with valid user data.
        """
        response = self.client.get(reverse("profiles:profile", kwargs={"username": self.user1.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_view_context_data(self):
        """
        Test that the profile view provides the correct context data.
        """
        response = self.client.get(reverse("profiles:profile", kwargs={"username": self.user1.username}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["profile"], self.profile1)

    # Integration Tests
    def test_index_integration(self):
        """
        Test the index page integration by verifying the HTTP status code.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)

    def test_profile_integration_valid_user(self):
        """
        Test the profile view integration for a valid username.
        """
        response = self.client.get(reverse("profiles:profile", kwargs={"username": self.user2.username}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New York")  # Validate profile content in the response

    def test_profile_integration_invalid_user(self):
        """
        Test the profile view integration for an invalid username.
        """
        response = self.client.get(reverse("profiles:profile", kwargs={"username": "nonexistentuser"}))
        self.assertEqual(response.status_code, 404)
