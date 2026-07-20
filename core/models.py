# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    id_equipe = models.ForeignKey('Equipe', models.DO_NOTHING, db_column='id_equipe')
    id_responsavel = models.ForeignKey('Responsavel', models.DO_NOTHING, db_column='id_responsavel')
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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    nome = models.CharField(unique=True, max_length=100)
    permisao1 = models.BooleanField()
    permisao2 = models.BooleanField()
    permisao3 = models.BooleanField()
    permisao4 = models.BooleanField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cargo'


class Comunicado(models.Model):
    id_autor = models.ForeignKey('Equipe', models.DO_NOTHING, db_column='id_autor')
    titulo = models.CharField(max_length=200)
    mensagem = models.TextField()
    destinatario = models.CharField(max_length=10)
    id_turma = models.IntegerField(blank=True, null=True)
    publicar_em = models.DateTimeField(blank=True, null=True)
    publicado = models.BooleanField()
    visivel_site = models.BooleanField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comunicado'


class ConfiguracaoSite(models.Model):
    chave = models.CharField(unique=True, max_length=100)
    valor = models.TextField(blank=True, null=True)
    atualizado_em = models.DateTimeField()
    atualizado_por = models.ForeignKey('Equipe', models.DO_NOTHING, db_column='atualizado_por', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuracao_site'


class Curso(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True, null=True)
    carga_horaria = models.IntegerField()
    publico_alvo = models.CharField(max_length=200, blank=True, null=True)
    pre_requisito = models.CharField(max_length=200, blank=True, null=True)
    visivel_site = models.BooleanField()
    ativo = models.BooleanField()
    criado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'curso'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipe(models.Model):
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    nome_completo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    ativo = models.BooleanField()
    criado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equipe'


class Frequencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_horario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='id_horario')
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    data_aula = models.DateField()
    status = models.CharField(max_length=15)
    justificativa = models.TextField(blank=True, null=True)
    registrado_por = models.ForeignKey(Equipe, models.DO_NOTHING, db_column='registrado_por')
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'frequencia'


class Horario(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    id_professor = models.ForeignKey(Equipe, models.DO_NOTHING, db_column='id_professor')
    dia_semana = models.CharField(max_length=3)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    sala = models.CharField(max_length=60, blank=True, null=True)
    publicado = models.BooleanField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'horario'


class LeituraComunicado(models.Model):
    id_comunicado = models.ForeignKey(Comunicado, models.DO_NOTHING, db_column='id_comunicado')
    id_usuario = models.IntegerField()
    lido_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leitura_comunicado'
        unique_together = (('id_comunicado', 'id_usuario'),)


class LogAuditoria(models.Model):
    id_equipe = models.ForeignKey(Equipe, models.DO_NOTHING, db_column='id_equipe', blank=True, null=True)
    acao = models.CharField(max_length=100)
    tabela_afetada = models.CharField(max_length=80, blank=True, null=True)
    dados_anteriores = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_auditoria'


class Matricula(models.Model):
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    data_inicio = models.DateField()
    data_saida = models.DateField()
    status = models.CharField(max_length=15)
    criado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'matricula'
        unique_together = (('id_aluno', 'id_turma'),)


class ProfessorTurma(models.Model):
    id_equipe = models.ForeignKey(Equipe, models.DO_NOTHING, db_column='id_equipe')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma')
    criado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'professor_turma'
        unique_together = (('id_equipe', 'id_turma'),)


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


class Turma(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')
    nome_turma = models.CharField(max_length=80)
    limite_alunos = models.IntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    ativo = models.BooleanField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'turma'
