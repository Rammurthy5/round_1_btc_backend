import os
import secrets
import string

from django.http import HttpResponseNotAllowed, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from constants import ALPHAVANTAGE_KEY
from utils import HashApiKey
from .exchange_rate_service import ExchangeRateService
from .models import ExchangeRate, ApiKey


@api_view(['GET'])
def generate_apikey(request):
    apikey = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(15))
    api_key_model = ApiKey()
    api_key_model.hashed_key = HashApiKey(apikey)
    api_key_model.save()
    return Response(apikey)


@api_view(['GET', 'POST'])
def quotes(request):
    if request.method == 'GET':
        try:
            return Response(ExchangeRateService.get_latest_quote())
        except ExchangeRate.DoesNotExist:
            raise Http404
    elif request.method == 'POST':
        exchange_rate_service = ExchangeRateService(api_token=os.environ.get(ALPHAVANTAGE_KEY))
        exchange_rate_service.update_latest_quote()
        return Response('success')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
