from django.db import models
from pessoa.models import Fornecedor

# Create your models here.
class Produto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name='produtos')
    nome_comercial = models.CharField(max_length=255)
    principio_ativo = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    forma_farmaceutica = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=50)
    codigo_barras = models.CharField(max_length=50, unique=True)
    receita_obrigatoria = models.BooleanField(default=False)
    tarja = models.CharField(
        max_length=20,
        choices=[
            ('sem', 'Sem tarja'),
            ('vermelha', 'Tarja vermelha'),
            ('preta', 'Tarja preta')
        ]
    )

    def __str__(self):
        return f"{self.nome_comercial} - {self.dosagem} ({self.fabricante})"

class EstoqueProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='estoques')
    numero_lote = models.CharField(max_length=50)
    data_validade = models.DateField()
    quantidade = models.PositiveIntegerField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    local_armazenamento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.produto.nome_comercial} - Lote {self.numero_lote}"

class MovimentacaoEntrada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='entradas')
    data_entrada = models.DateField(auto_now_add=True)
    quantidade = models.PositiveIntegerField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    forma_aquisicao = models.CharField(
        max_length=50,
        choices=[
            ('compra', 'Compra'),
            ('devolucao', 'Devolução'),
            ('doacao', 'Doação')
        ]
    )

    def __str__(self):
        return f"Entrada - {self.produto.nome_comercial} ({self.quantidade})"

class MovimentacaoSaida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='saidas')
    data_saida = models.DateField(auto_now_add=True)
    motivo = models.CharField(
        max_length=50,
        choices=[
            ('venda', 'Venda'),
            ('perda', 'Perda'),
            ('doação', 'Doação'),
            ('brinde', 'Brinde')
        ]
    )
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Saída - {self.produto.nome_comercial} ({self.motivo})"
