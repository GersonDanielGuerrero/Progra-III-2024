from django.urls import path
from .views import CarritoProductoView

urlpatterns = [
    path('carrito', CarritoProductoView.as_view()),
]
