from django.db import models
from baseapp.models import BaseModel
from accounts.models import CustomUser
# Create your models here.

class Categoriy(BaseModel):
    title = models.CharField(max_length=123)
    desc = models.CharField(max_length=123)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, blank=True,null=True)
    image = models.ImageField(upload_to='catigories/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Color(BaseModel):
    name = models.CharField(max_length=150)



    def __str__(self):
        return self.name

class Size(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Product(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='products')
    title = models.CharField(max_length=120)
    short_desc = models.CharField(max_length=120)
    desc = models.TextField()
    info = models.TextField()
    image = models.ImageField(upload_to='products/')
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    quantity = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Categoriy,on_delete=models.CASCADE,related_name='products')


    def __str__(self):
        return self.title

    