from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class Usuario(AbstractUser, PermissionsMixin):
    pass


class Equipe(models.Model):
    nome_completo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    ativo = models.BooleanField()
    criado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipe'


class Responsavel(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(unique=True, max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=150, blank=True, null=True)
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'responsavel'


class Aluno(models.Model):
    id_equipe = models.ForeignKey(Equipe, models.DO_NOTHING, db_column='id_equipe')
    id_responsavel = models.ForeignKey(Responsavel, models.DO_NOTHING, db_column='id_responsavel')
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    ativo = models.BooleanField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'aluno'