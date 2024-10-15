from django.db import models

class Market(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qtd_est = models.IntegerField()
    date_criation = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.name