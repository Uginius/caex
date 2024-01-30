from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    crypto_exchange = models.BooleanField(default=False, verbose_name='Cryptocurrency Exchange')
    foreign_exchange = models.BooleanField(default=False, verbose_name='Foreign Currency Exchange')
    bank_account = models.BooleanField(default=False, verbose_name='Bank Account (Powered by Neobank Solution)')
    money_transfer = models.BooleanField(default=False, verbose_name='Money Transfer')

    def __str__(self):
        return f'ID: {self.user.pk} CE: {self.crypto_exchange} FE: {self.foreign_exchange}'
