from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
from . import views

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get('/chat/dankman558/')
        self.assertEquals(response.status_code, 200)

class badInputTests(SimpleTestCase):

    def test_view_url_by_name(self):
        badInputs = ['^&*%#$&@#$@@124', '_____   1234!@#$', 'asdf', "bonkman"]


        for badInput in badInputs:

            response = self.client.get('/chat/' + badInput + '/')
            print(badInput)
            
            self.assertEquals(response.status_code, 200)

      


                

