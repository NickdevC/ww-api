from django.contrib.auth.models import User
from .models import Adventure
from rest_framework import status
from rest_framework.test import APITestCase


class AdventureListViewsTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='nick', password='pass')
    
    def test_can_list_posts(self):
        nick = User.objects.get(username='nick')
        Adventure.objects.create(owner=nick, title='a test title')
        response = self.client.get('/adventures/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/adventures/', {'title': 'a test title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AdventureDetailViewTests(APITestCase):
    def setUp(self):
        nick = User.objects.create_user(username='nick', password='pass')
        chloe = User.objects.create_user(username='chloe', password='pass')
        Adventure.objects.create(
            owner=nick, title='a test title', description='nicks content'
        )
        Adventure.objects.create(
            owner=chloe, title='another test title', description='chloes content'
        )
    
    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/adventures/1/')
        self.assertEqual(response.data['title'], 'a test title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_using_invalid_valid_id(self):
        response = self.client.get('/adventures/50/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
