from django.urls import path
from .views import RegistroView, LoginView, DireccionesView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('registro/', RegistroView.as_view()),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('direcciones/', DireccionesView.as_view()),
]