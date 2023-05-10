from django.contrib.auth.models import User
from .models import Adventure
from rest_framework import status
from rest_framework.test import APITestCase


class AdventureList(APITestCase):
    def setUp(self):
        User.objects.create_user(username='nick', password='pass')
    
    def test_can_list_posts(self):
        nick = User.objects.get(username='nick')
        Adventure.objects.create(owner=nick, title='a test title')
        response = self.client.get('/adventures/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
