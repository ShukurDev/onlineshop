from django.db import models
from accounts.models import Profile
from products.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cart_user')
    completed = models.BooleanField(default=False, null=True, blank=True)
    #date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.completed)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems', null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='producitems', null=True)
    quantity = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"cartitem -{str(self.quantity)}"

