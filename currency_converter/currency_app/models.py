from django.db import models

# Create your models here.
class CurrencyConversion(models.Model):
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
    amount = models.FloatField()
    converted_amount = models.FloatField(blank=True, null=True)
    conversion_rate = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.from_currency} → {self.to_currency}"