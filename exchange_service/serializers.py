from rest_framework.serializers import ModelSerializer

from .models import ExchangeRate, ApiKey


class ExchangeRateSerializer(ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('price', 'date')


class ApiKeySerializer(ModelSerializer):
    class Meta:
        model = ApiKey
        fields = ('hashed_key')
