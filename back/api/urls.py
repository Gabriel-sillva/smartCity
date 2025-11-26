from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbienteViewSet, SensorViewSet, HistoricoViewSet


router = DefaultRouter()
router.register('ambientes', AmbienteViewSet)
router.register('sensores', SensorViewSet)
router.register('historicos', HistoricoViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]