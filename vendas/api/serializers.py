from rest_framework import serializers
from vendas.models import Venda, ItemVenda

class ItemVendaSerializer(serializers.ModelSerializer):
    produto_nome = serializers.ReadOnlyField(source='produto.nome')
    subtotal = serializers.ReadOnlyField()
    
    class Meta:
        model = ItemVenda
        fields = '__all__'
        extra_kwargs = {
            'venda': {'help_text': 'Venda à qual este item pertence'},
            'produto': {'help_text': 'Produto vendido'},
            'quantidade': {'help_text': 'Quantidade do produto vendido'},
            'preco_unitario': {'help_text': 'Preço unitário do produto no momento da venda'}
        }

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True, read_only=True)
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')
    funcionario_nome = serializers.ReadOnlyField(source='funcionario.nome')
    valor_total = serializers.ReadOnlyField()
    
    class Meta:
        model = Venda
        fields = '__all__'
        extra_kwargs = {
            'cliente': {'help_text': 'Cliente que realizou a compra'},
            'funcionario': {'help_text': 'Funcionário que registrou a venda'},
            'data_venda': {'help_text': 'Data e hora da venda (formato YYYY-MM-DD HH:MM:SS)'},
            'forma_pagamento': {'help_text': 'Forma de pagamento utilizada (ex: Dinheiro, Cartão, Pix)'}
        }