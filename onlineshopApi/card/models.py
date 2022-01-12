from django.db import models
from accounts.models import BaseUser
from products.models import Product


# Create your models here.
class Card(models.Model):
    STATUS = {
        ('New', 'New'),
        ('Waiting', 'Waiting'),
        ('approved', 'approved'),
    }
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='card_user')
    completed = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(choices=STATUS, null=True, max_length=80, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class CardItem(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='carditems', null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='producitems', null=True)
    quantity = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.card.name} {self.product.name}"

