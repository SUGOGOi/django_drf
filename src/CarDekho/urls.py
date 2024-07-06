
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.test_api, name='test_api'),
    path("car/", include('CarDekho_app.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
