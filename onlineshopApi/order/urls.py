from django.urls import path
from . import views

urlpatterns = [
    path('orders', views.OrderView.as_view()),
    path('ordercreate/', views.OrderView.as_view()),
    path('orders/<int:pk>', views.OrderDetailView.as_view()),

    path('orderitem', views.OrderItemView.as_view()),
    path('orderitemstatis/', views.OrderItemStatis.as_view()),
]