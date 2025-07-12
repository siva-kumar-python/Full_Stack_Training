from django.db import models

# Create your models here.
class Canteen(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='canteen/', blank=True, null=True)

    def __str__(self):
        return self.name
