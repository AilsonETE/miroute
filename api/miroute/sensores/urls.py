from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DadosSensorViewSet

router = DefaultRouter()
router.register(r'sensores', DadosSensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
