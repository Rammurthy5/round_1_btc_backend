import requests

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ExchangeRateService(metaclass=Singleton):
    def __init__(self, api_token):
        print('ExchangeRateService init')
        self.api_token = api_token
        self.endpoint = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
        self.target_currency = 'USD'

    def get_currency_exchange_rate_in_usd(self, currency):
        response = requests.get('{}&from_currency={}&to_currency={}&apikey={}'.format(
            self.endpoint,
            currency,
            self.target_currency,
            self.api_token
        ))
        if response.status_code == 200:
            return response.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']
        return None

    def update_currency_exchange_rate_in_usd(self, currency):
        exchange_rate = self.get_currency_exchange_rate_in_usd(currency)

        exchange_rate_model = ExchangeRate()
        exchange_rate_model.currency = currency
        exchange_rate_model.price = exchange_rate
        exchange_rate_model.save()

    @staticmethod
    def get_latest_quote():
        print("get latest quote")
        exchange_rate = ExchangeRate.objects.latest('date')
        return ExchangeRateSerializer(exchange_rate).data

    def update_latest_quote(self):
        self.update_currency_exchange_rate_in_usd('BTC')
