from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.professional_profile import ProfessionalProfile

CREATE_PROFESSIONAL_PROFILE_URL = reverse("professional_profile:professional-profile-create")
RETRIEVE_PROFESSIONAL_PROFILE_URL = reverse("professional_profile:professional-profile-detail", kwargs={'pk': 1})

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProfessionalProfileTest(TestCase):
    
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
        self.pp_created = ProfessionalProfile.objects.create(
            headline="headline",
            current_position="current_position",
            description="description",
            date_begin="2015-03-12",
            date_end="2020-09-13",
            photo="photo",
            experience_years=4,
            user=self.user
        )

    def test_create_professional_profile(self):
        payload = {
            "address": "address",
            "street": "street",
            "cellphone": "cellphone",
            "email": "me@yopmail.com",
            "headline":"headline",
            "current_position":"current_position",
            "description":"description",
            "date_begin":"2015-03-12",
            "date_end":"2020-09-13",
            "photo":"photo",
            "experience_years": 5,
            "user":self.user
        }        
        res = self.client.post(CREATE_PROFESSIONAL_PROFILE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list_professional_profile(self):
        res = self.client.get(CREATE_PROFESSIONAL_PROFILE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_professional_profile(self):
        res = self.client.get(
            reverse("professional_profile:professional-profile-detail",
                    kwargs={'pk': self.pp_created.id}) 
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_invalid_professinal_profile(self):
        res = self.client.get(RETRIEVE_PROFESSIONAL_PROFILE_URL)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_professional_profile(self):
        payload = {
            "address": "address",
            "street": "street",
            "cellphone": "cellphone",
            "email": "me@yopmail.com",
            "headline": "headline updated",
            "current_position": "current_position",
            "description": "description update",
            "date_begin": "2015-03-12",
            "date_end": "2020-09-13",
            "photo": "photo",
            "experience_years": 8,
            "user": self.user
        }
        res = self.client.put(
            reverse("professional_profile:professional-profile-detail",
                    kwargs={'pk': self.pp_created.id}),
            data=payload
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_professional_profile(self):
        res = self.client.delete(
            reverse("professional_profile:professional-profile-detail",
                    kwargs={'pk': self.pp_created.id})
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
