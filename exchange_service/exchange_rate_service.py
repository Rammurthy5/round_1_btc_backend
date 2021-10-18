from typing import Callable

from .usd_exchange import USDExchangeRateService

def client_code(api_token, target_currency='USD') -> Callable:
    if target_currency.upper()=='USD':
        return USDExchangeRateService(api_token)
