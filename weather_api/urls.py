from django.urls import path, include
from weather_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('descriptions', views.DescriptionViewSet)

urlpatterns = [
    path('', include(router.urls))
]