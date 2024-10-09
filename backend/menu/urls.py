from django.urls import path
from .views import CategoriaView, ListaProductosView

urlpatterns = [
    path('categorias/', CategoriaView.as_view()),
    path('productos/', ListaProductosView.as_view()),
]