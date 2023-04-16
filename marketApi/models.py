from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Trade(models.Model):
    ticker = models.CharField(max_length=10, null=False, blank=False)
    price = models.FloatField(null=False, blank=True, default=False)
    # method = models.CharField(max_length=10, null=False, blank=True)
    outcome = models.CharField(max_length=10, null=False, blank=True)
    comment = models.TextField(null=False, blank=True)
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=False)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=False)
    user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, verbose_name='User', related_name='portfolios')

    def __str__(self):
        return self.ticker
