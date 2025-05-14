from rest_framework import viewsets
from pessoa.models import Cliente, Funcionario, Cargo
from pessoa.api.serializers import ClienteSerializer, FuncionarioSerializer, CargoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Clientes.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Funcionários.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class CargoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite operações CRUD em Cargos.
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer