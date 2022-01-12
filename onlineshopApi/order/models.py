from django.db import models
from accounts.models import BaseUser
from products.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='order_user')
    ordered = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    barcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Order -> by {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.BigIntegerField(null=True, blank=True, verbose_name='order_item_qantity')
    date_added = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        if self.date_added:
            return self.date_added
        else:
            return super.__str__()

