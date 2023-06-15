from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=250,null = True)
    description = models.TextField(null = True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100,null = True)
    images = models.ImageField()

    def __str__(self):
        return self.title


