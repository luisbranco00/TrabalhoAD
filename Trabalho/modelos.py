from django.forms import models
from django.contrib.auth.models import User
from django.db import models


class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField("Nome", max_length=60)
    data_nascimento = models.CharField("data_nascimento", max_length=10)
    n_cont = models.CharField("Numero de Contribuinte", unique=True, max_lenght=9)
    n_cc = models.CharField("Numero Cartao Cidadao", unique=True, max_length=8)

    def __str__(self):
        return f"Nome : {self.nome}, Type: {self.permissao}"


class Utilizador(Funcionario):
    Permissao = [('A', 'Administrador'), ('M', 'Medico'), ('F', 'Farmaceutico')]
    permissao = models.CharField("Type", max_length=1, choices=Permissao)


class Utente(Funcionario):
    id_Utente = models.AutoField(primary_key=True)
    def __str__(self):
        return f"Nome: {self.nome}"


class Medicamentos(models.Model):
    id_med = models.AutoField(primary_key=True)
    descrição = models.CharField("Descrição", max_length=50)
    quantidade = models.CharField("Quantidade em Stock", max_length=4)
    quantidade_minima = models.CharField("Quantidade Minima", max_length=4)
    id_fornecedor=models.CharField("Id Fornecedor",max_length=5)

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Utilizador(permissao="M"), verbose_name= "Funcionario", on_delete=models.PROTECT)
    utente = models.ForeignKey(Utente(), verbose_name="Utente", on_delete=models.PROTECT)
    descricao = models.CharField("Descrição da consulta", max_length=80)
    data_realização= models.DateTimeField(null=False, blank=False, auto_now_add=True)

class Prescrição(models.Model):
    id_prescrição= models.AutoField(primary_key=True)
    farmaceutico=models.ForeignKey(Utilizador(permissao="F"), verbose_name="Funcionario", on_delete=models.PROTECT)
    utente = models.ForeignKey(Utente(), verbose_name="Utente", on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamentos(), verbose_name="Medicamento", on_delete=models.PROTECT)
    data = models.DateTimeField(null=False, blank=False, auto_now_add=True)













