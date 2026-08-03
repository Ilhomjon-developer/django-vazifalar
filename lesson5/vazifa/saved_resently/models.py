from django.db import models
from products.models import Product
from accounts.models import CustomUser
from baseapp.models import BaseModel
# Create your models here.


class Saved(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


    class Meta:
        unique_together = {'user','product'}