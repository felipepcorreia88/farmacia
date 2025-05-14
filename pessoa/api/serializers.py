from rest_framework import serializers
from pessoa.models import Cliente, Funcionario, Cargo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        extra_kwargs = {
            'nome': {'help_text': 'Nome completo do cliente'},
            'cpf': {'help_text': 'CPF do cliente (apenas números)'},
            'data_nascimento': {'help_text': 'Data de nascimento do cliente (formato YYYY-MM-DD)'},
            'telefone': {'help_text': 'Telefone de contato do cliente'},
            'email': {'help_text': 'Email do cliente'},
            'endereco': {'help_text': 'Endereço completo do cliente'}
        }

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
        extra_kwargs = {
            'nome': {'help_text': 'Nome do cargo'},
            'descricao': {'help_text': 'Descrição das atribuições do cargo'}
        }

class FuncionarioSerializer(serializers.ModelSerializer):
    cargo_nome = serializers.ReadOnlyField(source='cargo.nome')
    
    class Meta:
        model = Funcionario
        fields = '__all__'
        extra_kwargs = {
            'nome': {'help_text': 'Nome completo do funcionário'},
            'cpf': {'help_text': 'CPF do funcionário (apenas números)'},
            'data_nascimento': {'help_text': 'Data de nascimento do funcionário (formato YYYY-MM-DD)'},
            'telefone': {'help_text': 'Telefone de contato do funcionário'},
            'email': {'help_text': 'Email do funcionário'},
            'endereco': {'help_text': 'Endereço completo do funcionário'},
            'cargo': {'help_text': 'Cargo do funcionário na empresa'},
            'data_admissao': {'help_text': 'Data de admissão do funcionário (formato YYYY-MM-DD)'},
            'salario': {'help_text': 'Salário mensal do funcionário em reais'}
        }