from django.urls import path
from rest_framework_simplejwt import views as jwt

from auth.views import RegisterView

urlpatterns = [
    path('login/', jwt.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register')
]