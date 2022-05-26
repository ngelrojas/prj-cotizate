from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse("user:create")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserManagerTests(TestCase):
    """test manager user"""

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="angel@yopmail.com", password="me123456")
        self.assertEqual(user.email, "angel@yopmail.com")
        self.assertFalse(user.is_activate)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser("admin@yopmail.com", "admin2021")
        self.assertEqual(admin_user.email, "admin@yopmail.com")
        self.assertTrue(admin_user.is_activate)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class UserTest(TestCase):
    def setUp(self):
        data = {
            "email": "ngel@yopmail.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "rojas",
        }
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_valid_user_success(self):
        """test create new user"""
        payload = {
            "email": "me@yopmail.com",
            "password": "me123456",
            "first_name": "angel",
            "last_name": "rojas",
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_exists(self):
        """test user exists"""
        payload = {"email": "me@yopmail.com", "password": "me123456"}
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """test user create password too short"""
        payload = {"email": "me@yopmail.com", "password": "me123456"}
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)

    def test_update_data_user(self):
        """test update data current user"""
        payload = {
            "first_name": "angel",
            "last_name": "rojas",
            "password": "me123456",
            "email": "me@yopmail.com",
        }
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, payload["first_name"])
        self.assertTrue(self.user.check_password(payload["password"]))
