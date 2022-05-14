from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.profile_company import ProfileCompany

CREATE_PROFILE_COMPANY_URL = reverse("profile_company:profile-company-create")
RETRIEVE_PROFILE_COMPANY_URL = reverse("profile_company:profile-company-detail", kwargs={'pk': 1})

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProfileCompanyTest(TestCase):
    
    def setUp(self):
        data = {
            'email': 'ngel@cotizate.com',
            'password': 'me1234',
            'first_name': 'admin',
            'last_name': 'cotizate'
        }
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.created = ProfileCompany.objects.create(
            name="headline",
            photo="photo",
            nit="1282udud",
            user=self.user
        )

    def test_create_profile_company(self):
        payload = {
            "address": "address",
            "street": "street",
            "cellphone": "cellphone",
            "email": "me@yopmail.com",
            "description": "description",
            "name":"headline",
            "photo":"photo",
            "nit":"1282udud",
            "user":self.user 
        }
        res = self.client.post(CREATE_PROFILE_COMPANY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list_profiles_company(self):
        res = self.client.get(CREATE_PROFILE_COMPANY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_profiles_company(self):
        res = self.client.get(
            reverse("profile_company:profile-company-detail",
                    kwargs={'pk': self.created.id})
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_profile_company(self):
        payload = {
            "address": "address",
            "street": "street",
            "cellphone": "cellphone",
            "email": "me@yopmail.com",
            "description": "description",
            "name":"headline",
            "photo":"photo",
            "nit":"1282udud",
            "user":self.user 
        }
        res = self.client.put(
            reverse("profile_company:profile-company-detail",
                    kwargs={'pk': self.created.id}),
            data=payload
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_profile_company(self):
        res = self.client.delete(
            reverse("profile_company:profile-company-detail",
                    kwargs={'pk': self.created.id})
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
