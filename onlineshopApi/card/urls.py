from django.urls import path
from . import views

urlpatterns = [
    path('cartitem', views.CartItemView.as_view()),
]