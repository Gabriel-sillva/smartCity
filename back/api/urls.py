from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbienteViewSet, SensorViewSet, HistoricoViewSet

# =====================================================================
# Router principal — registra todas as rotas CRUD automaticamente
# =====================================================================
router = DefaultRouter()
router.register(r'ambientes', AmbienteViewSet)
router.register(r'sensores', SensorViewSet)
router.register(r'historicos', HistoricoViewSet)

# =====================================================================
# Inclui todas as rotas geradas pelos ViewSets
# =====================================================================
urlpatterns = [
    path('', include(router.urls)),
]
