from django.db import models

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=255, verbose_name="Nome Fantasia")
    endereco = models.TextField(verbose_name="Endereço")

    def __str__(self):
        return f"{self.nome_fantasia} ({self.cnpj})"
    
class Cliente(models.Model):
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")  # Ex: 000.000.000-00
    telefone = models.CharField(max_length=20, blank=True, verbose_name="Telefone")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    endereco = models.TextField(verbose_name="Endereço")

    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"

