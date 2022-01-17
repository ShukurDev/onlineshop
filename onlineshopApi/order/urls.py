from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.OrderListCreateView.as_view()),
    path('orders/<int:pk>', views.OrderDetailView.as_view()),
    path('order/info', views.OrderStatisView.as_view()),

    # orderitem urls

    path('orderitem', views.OrderItemView.as_view()),
    #path('orderitem/serializer', )
]