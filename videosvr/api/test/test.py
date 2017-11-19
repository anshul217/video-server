from __future__ import absolute_import
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import *
from rest_framework.authtoken.models import Token

class UserAPITest(APITestCase):

    def setupUser(self):
        '''
        Setting up user object.
        '''
        user_obj=User.objects.create(
                                     username="anshul@gmail.com",
                                     email="anshul@gmail.com",
                                     )
        
        user_obj.set_password("anshul@123")
        
        user_obj.save()
        
        
        self.token, created = Token.objects.get_or_create(user=user_obj)
        
         
    def tearDown(self):
        '''
        clearing user objects.
        '''
        User.objects.all().delete()

 
    def test_user_login(self):
        """
        Ensure we can create a new user object.
        """
        self.setupUser()
        data = {
                'email':'anshul@gmail.com',
                'password':'anshul@123'
                }
        
        response = self.client.post(
                                    '/user/login/',
                                    data,
                                    format='json'
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "anshul@gmail.com")
        self.tearDown()

 