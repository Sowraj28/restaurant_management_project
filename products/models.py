from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)


class CardItem(models.Model):
    name=models.Foreignkey(User,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=200)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item_name}{self.quantity}"
        