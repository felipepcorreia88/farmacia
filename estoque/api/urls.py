from django.urls import path, include
from rest_framework.routers import DefaultRouter
from estoque.api.views import ProdutoViewSet, CategoriaViewSet, FornecedorViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'fornecedores', FornecedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]