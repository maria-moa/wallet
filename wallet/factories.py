from django.contrib.auth import get_user_model
from wallet_app.models import Wallet
import factory
from factory.django import DjangoModelFactory
from transaction.models import Transaction

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.sequence(lambda n: "user_{}".format(n))
    first_name = "John"
    last_name = "Doe"
    email = factory.sequence(lambda n: "test{}@example.com".format(n))
    password = "password"


class WalletFactory(DjangoModelFactory):
    class Meta:
        model = Wallet

    owner = factory.SubFactory(UserFactory)
    balance = 100


class TransactionsFactory(DjangoModelFactory):
    class Meta:
        model = Transaction

    tracker_id = factory.sequence(lambda n: n)
