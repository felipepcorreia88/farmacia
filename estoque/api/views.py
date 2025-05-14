from rest_framework import viewsets
from estoque.models import Produto, Categoria, Fornecedor
from estoque.api.serializers import ProdutoSerializer, CategoriaSerializer, FornecedorSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Produtos.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Categorias.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Fornecedores.
    """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer