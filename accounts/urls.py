from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserProfileViewSet

router = DefaultRouter()
router.register(r'user', UserProfileViewSet)

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # To refresh access token
    # Add other URLs as needed
    path('', include(router.urls)),

]
