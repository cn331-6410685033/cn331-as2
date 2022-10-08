from collections import UserString
from unittest.util import _MAX_LENGTH
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


# Create your tests here.

class UsersTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username="Earth",password="Ironman1234",)
        
    def test_login_success(self):
        self.client.login(username="Earth",password="Ironman1234")
        user = User.objects.first()
        self.client.get(reverse("index"))

    def test_login_fail(self):
        self.client.login(username="Earth",password="Batman1234")
        user = User.objects.first()
        self.client.get(reverse("login"))

    def test_not_login(self):
        user = User.objects.first()
        self.client.get(reverse("login"))

    def test_logout(self):
        self.client.login(username="Earth",password="Ironman1234")
        user = User.objects.first()
        self.client.get(reverse("index"))
        self.client.logout()
        user = User.objects.first()
        self.client.get(reverse("login"))

     

        