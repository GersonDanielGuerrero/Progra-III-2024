from django.urls import path
from .views import RegistroView, DireccionView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('registro/', RegistroView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('direcciones/', DireccionView.as_view()),
    path('direcciones/<int:id>/', DireccionView.as_view()),
]