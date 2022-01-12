from django.contrib import admin
from .models import Card, CardItem
# Register your models here.

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass

@admin.register(CardItem)
class CardItemAdmin(admin.ModelAdmin):
    pass
