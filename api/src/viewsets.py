from rest_framework import viewsets
from . import serializers
from api import models

class MarketViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MarketSerializer
    queryset = models.Market.objects.all()
    

