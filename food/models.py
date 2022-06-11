from django.db import models


# Create your models here.

class item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_discription = models.CharField(max_length=200)
    item_number = models.IntegerField()