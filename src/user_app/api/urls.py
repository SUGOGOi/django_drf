
from django.urls import path , include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework_simplejwt.views import TokenRefreshView    #,TokenObtainPairView

urlpatterns = [
    path("login", obtain_auth_token, name='login'),
    path("register", views.RegistrationView.as_view(), name='register'),
    path('logout', views.Logout_view.as_view(), name='logout'),
    # path('logout', views.logout_view, name='logout')
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
