from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendas.api.views import VendaViewSet, ItemVendaViewSet

router = DefaultRouter()
router.register(r'vendas', VendaViewSet)
router.register(r'itens', ItemVendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]