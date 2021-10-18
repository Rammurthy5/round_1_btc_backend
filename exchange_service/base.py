from abc import ABC, abstractmethod
from .serializers import ExchangeRateSerializer
from .models import ExchangeRate


class AbstractClass(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """
   
    # These operations have to be implemented in subclasses.

    @abstractmethod
    def update_currency_exchange_rate(self, currency) -> None:
        pass

    @abstractmethod
    def get_currency_exchange_rate(self, currency) -> None:
        pass

    # These are "hooks." Subclasses may override them, but it's not mandatory
    def get_latest_quote(self) -> None:
        exchange_rate = ExchangeRate.objects.latest('date')
        return ExchangeRateSerializer(exchange_rate).data

    def update_latest_quote(self, currency='BTC') -> None:
        self.update_currency_exchange_rate(currency)
        