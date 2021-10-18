from typing import Union, Any, List, Type, Dict

import requests

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from .base import AbstractClass


JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class USDExchangeRateService(AbstractClass):
    def __init__(self, api_token) -> None:
        self.api_token = api_token
        self.endpoint = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
        self.target_currency = 'USD'

    def get_currency_exchange_rate(self, currency) -> JSON:

        response = requests.get('{}&from_currency={}&to_currency={}&apikey={}'.format(
            self.endpoint,
            currency,
            self.target_currency,
            self.api_token
        ))
        if response.status_code == 200:
            return response.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']
        return None

    def update_currency_exchange_rate(self, currency) -> None:
        exchange_rate = self.get_currency_exchange_rate(currency)

        exchange_rate_model = ExchangeRate()
        exchange_rate_model.currency = currency
        exchange_rate_model.price = exchange_rate
        exchange_rate_model.save()

