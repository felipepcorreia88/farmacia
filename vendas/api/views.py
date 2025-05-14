from rest_framework import viewsets
from vendas.models import Venda, ItemVenda
from vendas.api.serializers import VendaSerializer, ItemVendaSerializer

class VendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Vendas.
    """
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Itens de Venda.
    """
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer