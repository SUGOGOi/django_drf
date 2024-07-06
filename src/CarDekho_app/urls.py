from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('showroom', views.Showroom_viewset,basename='showroom')
router.register('list', views.Car_viewset, basename='list')


urlpatterns = [
    # path("list", views.car_list_view, name="carlist"),
    # path("list/<int:pk>/", views.car_detail, name='cardetail'),
    # path("showroom", views.Showroom_list_view.as_view(), name="showroomlist"),
    # path('showroom/<int:showroom_id>/', views.Showroom_detail.as_view(), name='showroomdetail'),
    # path('',include(router.urls)),
    path('', include(router.urls )),
    # path('review', views.Reviewlist.as_view(), name='reviewlist'),
    # path('review/<int:pk>', views.Review_detail.as_view(), name='reviewdetail')
    path('showroom/<int:pk>/create-review', views.Review_create.as_view(), name='review_create'),
    path('showroom/<int:pk>/review', views.Reviewlist.as_view(), name='review_list'),
    path('showroom/review/<int:pk>', views.Review_detail.as_view(), name='review_detail'),
]
