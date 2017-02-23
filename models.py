# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Apostila(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=10)  # Field name made lowercase.
    paginas = models.DecimalField(db_column='Paginas', max_digits=4, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APOSTILA'


class ApresentacaoDigital(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APRESENTACAO_DIGITAL'


class AreaPesquisa(models.Model):
    id_area = models.CharField(db_column='Id_Area', primary_key=True, max_length=20)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AREA_PESQUISA'


class AreaCampo(models.Model):
    id_area = models.ForeignKey(AreaPesquisa, db_column='Id_Area')  # Field name made lowercase.
    id_campo = models.ForeignKey('CampoPesquisa', db_column='Id_Campo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area_Campo'


class AreaConcentracao(models.Model):
    id_areaconc = models.CharField(db_column='Id_AreaConc', primary_key=True, max_length=20)  # Field name made lowercase.
    modalidade = models.CharField(db_column='Modalidade', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area_Concentracao'


class AreaSerie(models.Model):
    id_areaconc = models.ForeignKey(AreaConcentracao, db_column='Id_AreaConc')  # Field name made lowercase.
    id_serie = models.ForeignKey('SerieDeDestino', db_column='Id_Serie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area_Serie'


class Associado(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto')  # Field name made lowercase.
    id_areaconc = models.ForeignKey(AreaConcentracao, db_column='Id_AreaConc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Associado'


class Cartilha(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARTILHA'


class Curso(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CURSO'


class CampoPesquisa(models.Model):
    id_campo = models.CharField(db_column='Id_Campo', primary_key=True, max_length=20)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Campo_Pesquisa'


class Dissertacao(models.Model):
    id_dissertacao = models.CharField(db_column='Id_Dissertacao', primary_key=True, max_length=20)  # Field name made lowercase.
    titulo = models.TextField(db_column='Titulo')  # Field name made lowercase.
    data_defesa = models.DateField(db_column='Data_Defesa')  # Field name made lowercase.
    resumo = models.TextField(db_column='Resumo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DISSERTACAO'


class DissertPalavra(models.Model):
    id_dissertacao = models.ForeignKey(Dissertacao, db_column='Id_Dissertacao')  # Field name made lowercase.
    id_palavra = models.ForeignKey('PalavraChave', db_column='Id_Palavra')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dissert_Palavra'


class Ementa(models.Model):
    id_produto = models.ForeignKey('PropostaDisciplina', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ementa'


class EstaAssociado(models.Model):
    id_pessoa = models.ForeignKey('Pessoa', db_column='Id_Pessoa')  # Field name made lowercase.
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto')  # Field name made lowercase.
    papel = models.CharField(db_column='Papel', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Esta_Associado'


class Hipertexto(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HIPERTEXTO'


class Ies(models.Model):
    id_ies = models.CharField(db_column='Id_IES', primary_key=True, max_length=20)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IES'


class IesLocalizacao(models.Model):
    id_ies = models.ForeignKey(Ies, db_column='Id_IES')  # Field name made lowercase.
    id_localizacao = models.ForeignKey('Localizacao', db_column='Id_localizacao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IES_Localizacao'


class Jogo(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=20)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=20)  # Field name made lowercase.
    numero_jogadores = models.DecimalField(db_column='Numero_Jogadores', max_digits=2, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JOGO'


class JogoDigital(models.Model):
    id_produto = models.ForeignKey(Jogo, db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    plataforma = models.CharField(db_column='Plataforma', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JOGO_DIGITAL'


class JogoTabuleiro(models.Model):
    id_produto = models.ForeignKey(Jogo, db_column='Id_Produto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JOGO_TABULEIRO'


class LivroParadidatico(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=10)  # Field name made lowercase.
    paginas = models.DecimalField(db_column='Paginas', max_digits=4, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LIVRO_PARADIDATICO'


class Localizacao(models.Model):
    id_localizacao = models.CharField(db_column='Id_localizacao', primary_key=True, max_length=20)  # Field name made lowercase.
    rua = models.CharField(db_column='Rua', max_length=50)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=30)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Localizacao'


class MaterialNecessario(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MATERIAL_NECESSARIO'


class Midia(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=10)  # Field name made lowercase.
    tamanho = models.CharField(db_column='Tamanho', max_length=20)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MIDIA'


class ModeloEducacional(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODELO_EDUCACIONAL'


class ObjetoEnsino(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OBJETO_ENSINO'


class Oficina(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    numero_encontros = models.DecimalField(db_column='Numero_Encontros', max_digits=2, decimal_places=0)  # Field name made lowercase.
    publico_alvo = models.CharField(db_column='Publico_Alvo', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OFICINA'


class PaginaWeb(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAGINA_WEB'


class Palestra(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    numero_encontros = models.DecimalField(db_column='Numero_Encontros', max_digits=2, decimal_places=0)  # Field name made lowercase.
    publico_alvo = models.CharField(db_column='Publico_Alvo', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PALESTRA'


class Pessoa(models.Model):
    id_pessoa = models.CharField(db_column='Id_Pessoa', primary_key=True, max_length=20)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_mail', max_length=50)  # Field name made lowercase.
    link_lattes = models.CharField(db_column='Link_Lattes', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PESSOA'


class PmpecTipo(models.Model):
    id_produto = models.ForeignKey('ProdutoMpec', db_column='Id_Produto')  # Field name made lowercase.
    id_tipo = models.ForeignKey('Tipo', db_column='Id_Tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PMPEC_Tipo'


class PreRequisito(models.Model):
    id_requisitos = models.CharField(db_column='Id_Requisitos', primary_key=True, max_length=20)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRE_REQUISITO'


class ProdutoMpec(models.Model):
    id_produto = models.DecimalField(db_column='Id_Produto', primary_key=True, max_digits=4, decimal_places=0)  # Field name made lowercase.
    id_ies = models.ForeignKey(Ies, db_column='Id_IES')  # Field name made lowercase.
    id_dissertacao = models.ForeignKey(Dissertacao, db_column='Id_Dissertacao')  # Field name made lowercase.
    nome_produto = models.TextField(db_column='Nome_Produto')  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase.
    objetivo = models.TextField(db_column='Objetivo')  # Field name made lowercase.
    tema_central = models.TextField(db_column='Tema_Central')  # Field name made lowercase.
    link_produto = models.TextField(db_column='Link_Produto', blank=True)  # Field name made lowercase.
    colaborador = models.TextField(db_column='Colaborador', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTO_MPEC'


class PropostaDisciplina(models.Model):
    id_produto = models.ForeignKey(ProdutoMpec, db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    periodo = models.CharField(db_column='Periodo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROPOSTA_DISCIPLINA'


class Prototipo(models.Model):
    id_produto = models.ForeignKey(ProdutoMpec, db_column='Id_Produto', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROTOTIPO'


class PalavraChave(models.Model):
    id_palavra = models.CharField(db_column='Id_Palavra', primary_key=True, max_length=20)  # Field name made lowercase.
    palavra = models.CharField(db_column='Palavra', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Palavra_Chave'


class Possui(models.Model):
    id_produto = models.ForeignKey(Curso, db_column='Id_Produto')  # Field name made lowercase.
    id_requisitos = models.ForeignKey(PreRequisito, db_column='Id_Requisitos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Possui'


class ProdutoTema(models.Model):
    id_produto = models.ForeignKey(ProdutoMpec, db_column='Id_Produto')  # Field name made lowercase.
    id_tema = models.ForeignKey('TemaAbordado', db_column='Id_Tema')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Produto_Tema'


class SequenciaDidatica(models.Model):
    id_produto = models.ForeignKey(ProdutoMpec, db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    numero_aulas = models.DecimalField(db_column='Numero_Aulas', max_digits=2, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEQUENCIA_DIDATICA'


class SerieDeDestino(models.Model):
    id_serie = models.CharField(db_column='Id_Serie', primary_key=True, max_length=20)  # Field name made lowercase.
    serie_de_destino = models.CharField(db_column='Serie_de_Destino', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Serie_de_Destino'


class TemaAbordado(models.Model):
    id_tema = models.CharField(db_column='Id_Tema', primary_key=True, max_length=20)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMA_ABORDADO'


class Texto(models.Model):
    id_produto = models.ForeignKey(ProdutoMpec, db_column='Id_Produto', primary_key=True)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEXTO'


class Tipo(models.Model):
    id_tipo = models.CharField(db_column='Id_Tipo', primary_key=True, max_length=20)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo'


class Vinculado(models.Model):
    id_pessoa = models.ForeignKey(Pessoa, db_column='Id_Pessoa')  # Field name made lowercase.
    id_area = models.ForeignKey(AreaPesquisa, db_column='Id_Area')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vinculado'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
