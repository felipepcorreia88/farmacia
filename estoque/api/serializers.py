from rest_framework import serializers
from estoque.models import Produto, Categoria, Fornecedor

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        extra_kwargs = {
            'nome': {'help_text': 'Nome da categoria do produto'},
            'descricao': {'help_text': 'Descrição detalhada da categoria'}
        }

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        extra_kwargs = {
            'nome': {'help_text': 'Nome do fornecedor'},
            'cnpj': {'help_text': 'CNPJ do fornecedor (apenas números)'},
            'telefone': {'help_text': 'Telefone de contato do fornecedor'},
            'email': {'help_text': 'Email do fornecedor'},
            'endereco': {'help_text': 'Endereço completo do fornecedor'}
        }

class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.ReadOnlyField(source='categoria.nome')
    fornecedor_nome = serializers.ReadOnlyField(source='fornecedor.nome')
    
    class Meta:
        model = Produto
        fields = '__all__'
        extra_kwargs = {
            'nome': {'help_text': 'Nome do produto'},
            'descricao': {'help_text': 'Descrição detalhada do produto'},
            'preco': {'help_text': 'Preço de venda do produto em reais'},
            'quantidade': {'help_text': 'Quantidade disponível em estoque'},
            'categoria': {'help_text': 'Categoria à qual o produto pertence'},
            'fornecedor': {'help_text': 'Fornecedor do produto'}
        }