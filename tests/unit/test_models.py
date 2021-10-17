from django.test import TestCase
from decimal import Decimal
from exchange_service.models import ApiKey, ExchangeRate


class ApiKeyTest(TestCase):
    """ Test module for ApiKey model """

    def setUp(self):
        ApiKey.objects.create(
            hashed_key='Casper')

    def test_api_key(self):
        api_key = ApiKey.objects.get(hashed_key='Casper')
        self.assertEqual(
            api_key.hashed_key, "Casper")
        self.assertEqual(
            api_key.invalid, False
        )
        self.assertIsNotNone(api_key.created)
        

class ExchangeRateTest(TestCase):
    """ Test module for ExchangeRate model """

    def setUp(self):
        ExchangeRate.objects.create(
            currency='AED', price=55.06)

    def test_exchange_rate(self):
        unit_val = ExchangeRate.objects.get(currency='AED')
        self.assertEqual(
            unit_val.currency, "AED")
        self.assertAlmostEqual(unit_val.price, Decimal(55.06))
        self.assertIsNotNone(unit_val.date)
