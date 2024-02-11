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


class CoinService(models.Model):
    title = models.CharField(max_length=250)
    caption = models.CharField(max_length=250, blank=True, null=True)
    icon = models.CharField(max_length=250, blank=True, null=True)
    is_banking = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.pk} Title: {self.title} Icon: {self.icon}'


class Step(models.Model):
    title = models.CharField(max_length=250)
    caption = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk} Title: {self.title} Icon: {self.icon}'

    class Meta:
        ordering = ['order', 'pk']
