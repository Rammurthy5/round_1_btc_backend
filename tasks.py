import os

from celery import Celery

from constants import ALPHAVANTAGE_KEY

app = Celery('tasks', backend='redis://redis:6379',
             broker='redis://redis:6379')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        3600.0, get_bitcoin_exchange_rate.s(), name='Get BTC exchange rate every hour')


@app.task
def get_bitcoin_exchange_rate():
    from exchange_service.exchange_rate_service import ExchangeRateService
    exchange_rate_service = ExchangeRateService(api_token=os.environ.get(ALPHAVANTAGE_KEY))
    exchange_rate_service.update_currency_exchange_rate_in_usd('BTC')
