from django.test import Client
from django.test import TestCase
from django.urls import reverse


class TestApikeyGenEndpoint(TestCase):
    def test_keygen(self):
        c = Client()
        response = c.get(reverse('generate-an-api-key'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.content)
