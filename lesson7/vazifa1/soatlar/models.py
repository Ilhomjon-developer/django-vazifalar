from django.db import models

class Watch(models.Model):
    title = models.CharField(max_length=150, verbose_name="Soat nomi")
    brand = models.CharField(max_length=100, verbose_name="Brend")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi ($)")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title