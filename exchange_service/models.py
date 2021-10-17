from django.db import models


# Create your models here.
class ExchangeRate(models.Model):
    currency = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class ApiKey(models.Model):
    hashed_key = models.CharField(max_length=255)
    invalid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hashed_key