from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.professional_profile import ProfessionalProfile
from core.profile_company import ProfileCompany
from core.social_network import SocialNetwork

CREATE_SOCIAL_NETWORK_URL = reverse("social_network:social-network-create")
RETRIEVE_SOCIAL_NETWORK_URL = reverse("social_network:social-network-detail", kwargs={'pk': 1})

def create_user(**params):
    return get_user_model().objects.create_user(**params)

def create_sn(**params):
    return SocialNetwork.objects.create(**params)


class SocialNetworkTest(TestCase):

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
        self.pp_id = 1 #professional_profile
        self.pc_id = 2 #profile_company
        self.sn_id = 1


    def test_create_social_network_professional_profile(self):
        payload = {
            "name": "linkedin",
            "profile": self.pp_id,
            "link": "https://linkedin.com"
        }
        res = self.client.post(CREATE_SOCIAL_NETWORK_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_social_network_profile_company(self):
        payload = {
            "name": "linkedin",
            "profile": self.pc_id,
            "link": "https://linkedin.com"
        }
        res = self.client.post(CREATE_SOCIAL_NETWORK_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list_social_networks(self):
        res = self.client.get(CREATE_SOCIAL_NETWORK_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_no_retrieve_professional_profile(self):
        res = self.client.get(f"user/social-network/{self.sn_id}?profile={self.pp_id}")
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_social_network(self):
        payload = {
            "name": "new twitter",
            "link": "new link here"
        }
        res = self.client.put(
            reverse("social_network:social-network-detail",
                    kwargs={'pk': self.sn_id}),
            data=payload
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_delete_social_network(self):
        res = self.client.delete(
            reverse("social_network:social-network-detail",
                    kwargs={'pk': self.sn_id})
        )
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
