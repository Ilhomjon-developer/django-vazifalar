from django.db import models
from baseapp.models import BaseModel
# Create your models here.

class Categoriy(BaseModel):
    title = models.CharField(max_length=123)
    desc = models.CharField(max_length=123)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, blank=True,null=True)


    def __str__(self):
        return self.title
    