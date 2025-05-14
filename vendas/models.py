from django.db import models
from pessoa.models import Cliente, Funcionario
from estoque.models import Produto

class Venda(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO_CREDITO', 'Cartão de Crédito'),
        ('CARTAO_DEBITO', 'Cartão de Débito'),
        ('PIX', 'Pix'),
        ('BOLETO', 'Boleto'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    data_venda = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_CHOICES)
    
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
    
    def __str__(self):
        return f"Venda {self.id} - {self.cliente.nome}"
    
    @property
    def valor_total(self):
        return sum(item.subtotal for item in self.itemvenda_set.all())

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Item de Venda'
        verbose_name_plural = 'Itens de Venda'
    
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
    
    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario