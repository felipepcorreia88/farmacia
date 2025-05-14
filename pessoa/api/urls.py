from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pessoa.api.views import ClienteViewSet, FuncionarioViewSet, CargoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'cargos', CargoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]