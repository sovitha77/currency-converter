from django.contrib import admin
from . models import CurrencyConversion
# Register your models here.
@admin.register(CurrencyConversion)
class CurrencyAdmin(admin.ModelAdmin):
  list_display = ("from_currency","to_currency","amount","converted_amount")