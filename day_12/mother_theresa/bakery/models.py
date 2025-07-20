from django.db import models

# Create your models here.
class Bakery(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='bakery/', blank=True, null=True)

    def __str__(self):
        return self.name
