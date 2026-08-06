from django.db import models
from baseapp.models import BaseModel
from accounts.models import CustomUser
from products.models import Product
# Create your models here.

class Card(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class CardItem(BaseModel):
    card = models.ForeignKey(Card,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.card


class Order(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    adress = models.CharField(max_length=120)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)



    @property
    def total_price(self):
        return sum(order_item.price for order_item in self.items)


    def __str__(self):
        return self.user


class OrderItem(BaseModel):
    order = models.ForeignKey(Card,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True,related_name='product_order')
    count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    @property
    def price(self):
        return self.count * self.product.price

    def __str__(self):
        return self.order