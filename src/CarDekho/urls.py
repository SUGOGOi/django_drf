
from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.test_api, name='test_api'),
    path("car/", include('CarDekho_app.urls')),
    path("account/", include('user_app.api.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
