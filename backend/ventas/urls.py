from django.urls import path
from .views import CarritoView

urlpatterns = [
path('carrito/', CarritoView.as_view()),
]
from django.urls import path
from .views import CarritoProductoView

urlpatterns = [
    path('carrito', CarritoProductoView.as_view()),
]
