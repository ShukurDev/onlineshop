from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.

@admin.register(Cart)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CardItemAdmin(admin.ModelAdmin):
    pass
