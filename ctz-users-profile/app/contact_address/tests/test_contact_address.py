from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.contact_address import ContactAddress

CREATE_CONTACT_ADDRESS_URL = reverse("contact_address:contact-address-create")
RETRIEVE_CONTACT_ADDRESS_URL = reverse("contact_address:contact-address-detail", kwargs={'pk': 1})

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ContactAddressTest(TestCase):
    
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
        self.contact_created = ContactAddress.objects.create(
            address="address created",
            street="street",
            cellphone="122345",
            email="email@yopmail.com",
            description="description",
            dni="1234556",
            user=self.user
        )

    def test_create_contact_address(self):
        payload = {
            "address": "this is an address for this test",
            "street": "this is street for this test",
            "cellphone": "1234567",
            "email": "angel@yopmail.com",
            "description": "description for this test",
            "dni":"123456",
            "user": self.user
        }
        res = self.client.post(CREATE_CONTACT_ADDRESS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list_contact_address(self):
        res = self.client.get(CREATE_CONTACT_ADDRESS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_contact_address(self):
        res = self.client.get(
            reverse("contact_address:contact-address-detail",
                    kwargs={'pk': self.contact_created.id})
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_invalid_contact_address(self):
        res = self.client.get(RETRIEVE_CONTACT_ADDRESS_URL)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_contact_address(self):
        payload = {
            "address": "this is an address for this test",
            "street": "this is street for this test",
            "cellphone": "1234567",
            "email": "angel@yopmail.com",
            "description": "description for this test",
            "dni":"123456",
            "user": self.user
        }
        
        res = self.client.put(
            reverse("contact_address:contact-address-detail",
                    kwargs={'pk': self.contact_created.id}),
            data=payload
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_contact_address(self):
        res = self.client.delete(
            reverse("contact_address:contact-address-detail",
                    kwargs={'pk': self.contact_created.id})
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
