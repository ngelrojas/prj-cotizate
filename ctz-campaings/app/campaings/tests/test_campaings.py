from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.campaing import Campaing

CREATE_CAMPAING = reverse("campaing:campaing-create")
CREATE_CAMPAING_LIST = reverse("campaing:campaing-list", kwargs={'pk': 1})
RETRIEVE_CAMPAING = reverse("campaing:campaing-detail", kwargs={'pk': 1})

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class CampaingTest(TestCase):
    
    def setUp(self):
        data = {
            'email': 'test@yopmail.com',
            'password': 'me123456',
            'first_name': 'jhon',
            'last_name': 'doe'
        }
        self.user = create_user(**data)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_create_campaing(self):
        payload = {
            "profile_id": 23, 
            "title" :"title", 
            "excerpt": "exceprt", 
            "description" : "description",
            "img_main":"img_main", 
            "url_video": "url_video", 
            "status": 2,
            "currency_id": 1, 
            "country_id": 2, 
            "city_id": 3, 
            "categor_ies": ["cate1", "cate2"], 
            "slogan_campaing": "slogan_campaing", 
        }
        message, created = Campaing.objects.update_or_create(payload)
        # res = self.client.post(CREATE_CAMPAING, payload)
        # self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(created, True)
        
    def test_list_campaing_with_profile_id(self):  
        res = self.client.get(CREATE_CAMPAING_LIST, kwargs={'pk': 1})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
