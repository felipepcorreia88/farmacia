from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField()
    
    class Meta:
        abstract = True

class Cliente(Pessoa):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    data_admissao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return self.nome