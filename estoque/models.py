from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField()
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.nome