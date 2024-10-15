from django.contrib import admin
from api import models
from .models import Market

@admin.register(models.Market)
class MarketAdmin(admin.ModelAdmin):
    ...
    # list_diplay = ('name', 'category', 'price', 'qtd_est',)
