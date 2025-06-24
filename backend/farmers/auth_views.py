from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .auth_serializers import EmailTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer

urlpatterns = [
    path('login/', EmailLoginView.as_view(), name='email_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
