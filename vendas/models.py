from django.db import models
from pessoa.models import Cliente
from estoque.models import Produto
from django.contrib.auth.models import User

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    produtos = models.ManyToManyField(Produto, through='ItemVenda')
    data_hora = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(
        max_length=20,
        choices=[
            ('dinheiro', 'Dinheiro'),
            ('credito', 'Cartão de Crédito'),
            ('debito', 'Cartão de Débito'),
            ('pix', 'Pix')
        ]
    )
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Venda #{self.id} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome_comercial} (Venda #{self.venda.id})"

class VendaReceita(models.Model):
    venda = models.OneToOneField(Venda, on_delete=models.CASCADE, primary_key=True)
    nome_medico = models.CharField(max_length=255)
    crm_uf = models.CharField(max_length=20, verbose_name="CRM e UF")
    imagem_receita = models.ImageField(upload_to='receitas/')
    data_prescricao = models.DateField()
    medicamento_prescrito = models.TextField()
    quantidade_prescrita = models.PositiveIntegerField()

    def __str__(self):
        return f"Receita - Venda #{self.venda.id}"

