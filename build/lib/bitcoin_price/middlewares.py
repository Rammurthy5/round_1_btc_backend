import os
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from constants import CUSTOM_TOKEN_HEADER, CUSTOM_TOKEN
from utils import HashApiKey
from exchange_service.models import ApiKey


class CheckTokenMiddleware(MiddlewareMixin):
    AUTHENTICATED_URLS = [
        '/api'
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        print(list(filter(request.path.startswith, self.AUTHENTICATED_URLS)))
        if list(filter(request.path.startswith, self.AUTHENTICATED_URLS)):
            if not request.headers.__contains__(CUSTOM_TOKEN_HEADER):
                return HttpResponse('Unauthorized', status=401)
            api_token = request.headers.get(CUSTOM_TOKEN_HEADER)
            
            exists = ApiKey.objects.filter(hashed_key = HashApiKey(api_token), invalid = False).exists()
            if not exists:
                return HttpResponse('Token mismatch', status=401)

        response = self.get_response(request)
        return response
