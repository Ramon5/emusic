from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from datetime import datetime
from decimal import Decimal
import datetime

# Create your models here.

UF = (
    ('MG', 'Minas Gerais'),
    ('SP', 'São Paulo'),
    ('RJ', 'Rio de Janeiro'),
    ('ES', 'Espirito Santo'),
    ('BA', 'Bahia'),
)

INSTRUMENTO = (
    ('ACORDEON', 'Acordeon'),
    ('BACK', 'Backing Vocal'),
    ('BAIXO', 'Baixo'),
    ('BATERIA', 'Bateria'),
    ('DJ', 'DJ'),
    ('GUITARRA', 'Guitarra'),
    ('VIOLAO/GUITARRA', 'Violão e Guitarra'),
    ('TECLADO', 'Teclado'),
    ('TROMPETE', 'Trompete'),
    ('TROMBONE', 'Trombone'),
    ('PERCUSSAO', 'Percussão'),
    ('SAX', 'Sax'),
    ('VIOLA', 'Viola'),
    ('VIOLAO', 'Violão'),
)

TIPOCONTRATACAO = (
    ('FREE', 'Free Lancer'),
    ('FIXO', 'Fixo Assalariado'),
)

ESPECIALIDADE = (
    ('ESTU', 'Estudio'),
    ('SHOW', 'Show'),
    ('ESSH', 'Show e Estudio'),

)

SCORE = (
    (1, '1 Estrela (Muito Ruim)'),
    (2, '2 Estrelas (Ruim)'),
    (3, '3 Estrelas (Medio)'),
    (4, '4 Estrelas (Bom)'),
    (5, '5 Estrelas (Muito Bom)'),

)

PRODUTOR = (
    ('EXECUTIVO', 'Produtor Executivo'),
    ('GERAL', 'Produtor Geral'),
    ('PALCO', 'Produtor de Palco'),
    ('TECNICO', 'Produtor Tecnico'),
    ('MUSICAL', 'Produtor Musical'),
    ('ARTISTICO', 'Artistico'),
)

TECNICO = (
    ('SOM', 'Tecnico de Som Palco e PA'),
    ('SOMP', 'Tecnico de Som PA'),
    ('SOMPL', 'Tecnico de Som Palco'),
    ('LUZ', 'Tecnico de Luz'),
    ('LED', 'Tecnico de LED - VJ'),
)

STAFF = (
    ('ROADIE', 'Roadie'),
    ('CARREGADOR', 'Carregador'),
    ('MOTORISTA', 'Motorista'),
    ('SEGURANCA', 'Segurança'),
    ('MAQUEADOR', 'Maqueador'),
    ('CABELEIREIRO', 'Cabeleireiro'),

)


class EmpresaContratante(models.Model):
    """Model definition for Contratante."""

    NomeEmpresa = models.CharField(
        'Nome da Empresa', blank=True, null=True, max_length=80)
    Score = models.IntegerField(
        'Score', blank=True, null=True, max_length=3, choices=SCORE)
    EnderecoEmpresa = models.CharField(
        'Endereço', blank=True, null=True, max_length=80)

    CidadeEmpresa = models.CharField(
        'Cidade', blank=True, null=True, max_length=80)
    CEPEmpresa = models.IntegerField(
        'CEP', blank=True, null=True, )
    UFEmpresa = models.CharField(
        'Estado', blank=True, null=True, max_length=3, choices=UF)

    EmailEmpresa = models.CharField(
        'Email', blank=True, null=True, max_length=80)
    TelefoneEmpresa = models.CharField(
        'Telefone', blank=True, null=True, max_length=80)
    Celular1Empresa = models.CharField(
        'Celular 1', blank=True, null=True, max_length=80)
    Celular2Empresa = models.CharField(
        'Celular 2', blank=True, null=True, max_length=80)
    Celular3Empresa = models.CharField(
        'Celular 3', blank=True, null=True, max_length=80)
    SiteEmpresa = models.CharField(
        'Site', blank=True, null=True, max_length=80)
    Instagram = models.CharField(
        'Instagram', blank=True, null=True, max_length=80)
    Facebook = models.CharField(
        'Facebook', blank=True, null=True, max_length=80)

    class Meta:
        """Meta definition for Contratante."""

        verbose_name = 'EmpresaContratante'
        verbose_name_plural = 'EmpresaContratantes'

    def __str__(self):

        return self.NomeEmpresa


class Contratante(models.Model):
    """Model definition for Contratante."""

    NomeContratante = models.CharField(
        'Nome do Contratante', blank=True, null=True, max_length=80)
    EmpresaContratante = models.ForeignKey(
        EmpresaContratante, on_delete=models.CASCADE)
    Score = models.IntegerField(
        'Score', blank=True, null=True, max_length=3, choices=SCORE)

    EmailContratante = models.CharField(
        'Email do Contratante', blank=True, null=True, max_length=80)
    Telefone = models.CharField(
        'Telefone', blank=True, null=True, max_length=80)
    Ramal = models.CharField(
        'Ramal', blank=True, null=True, max_length=80)
    Celular1 = models.CharField(
        'Celular 1', blank=True, null=True, max_length=80)
    Celular2 = models.CharField(
        'Celular 2', blank=True, null=True, max_length=80)
    Celular3 = models.CharField(
        'Celular 3', blank=True, null=True, max_length=80)
    Instagram = models.CharField(
        'Instagram', blank=True, null=True, max_length=80)
    Facebook = models.CharField(
        'Facebook', blank=True, null=True, max_length=80)
    Aniversario = models.DateField(
        'Aniversário', blank=True, null=True)

    class Meta:
        """Meta definition for Contratante."""

        verbose_name = 'Contratante'
        verbose_name_plural = 'Contratantes'

    def __str__(self):

        return self.NomeContratante


class Musico(models.Model):
    """Model definition for Contratante."""

    Nome = models.CharField(
        'Nome do Musico', blank=True, null=True, max_length=80)
    Instrumento = models.CharField(
        'Instrumento', blank=True, null=True, max_length=30, choices=INSTRUMENTO)
    Score = models.IntegerField(
        'Score', blank=True, null=True, max_length=3, choices=SCORE)
    Especialidade = models.CharField(
        'Especialidade', blank=True, null=True, max_length=4, choices=ESPECIALIDADE)
    TipoContratacao = models.CharField(
        'Tipo de Contrataçao', blank=True, null=True, max_length=4, choices=TIPOCONTRATACAO)
    ValorCache = models.DecimalField(
        'Valor', decimal_places=2, max_digits=10, blank=True, null=True)

    Email = models.CharField(
        'Email do Musico', blank=True, null=True, max_length=80)
    Telefone = models.CharField(
        'Telefone', blank=True, null=True, max_length=80)
    Celular1 = models.CharField(
        'Celular 1', blank=True, null=True, max_length=80)
    Celular2 = models.CharField(
        'Celular 2', blank=True, null=True, max_length=80)

    Instagram = models.CharField(
        'Instagram', blank=True, null=True, max_length=80)
    Facebook = models.CharField(
        'Facebook', blank=True, null=True, max_length=80)

    Endereco = models.CharField(
        'Endereço', blank=True, null=True, max_length=80)

    Cidade = models.CharField(
        'Cidade', blank=True, null=True, max_length=80)
    UF = models.CharField(
        'Estado', blank=True, null=True, max_length=3, choices=UF)
    CEP = models.IntegerField(
        'CEP', blank=True, null=True)

    Aniversario = models.DateField(
        'Aniversário', blank=True, null=True)

    class Meta:
        """Meta definition for Contratante."""

        verbose_name = 'Musico'
        verbose_name_plural = 'Musicos'

    def __str__(self):

        return self.Nome


class Produtor(models.Model):
    """Model definition for Contratante."""

    Nome = models.CharField(
        'Nome do Produtor', blank=True, null=True, max_length=80)
    DescricaoServico = models.CharField(
        'Descrição do Serviço', blank=True, null=True, max_length=30, choices=PRODUTOR)
    Score = models.IntegerField(
        'Score', blank=True, null=True, max_length=3, choices=SCORE)

    TipoContratacao = models.CharField(
        'Tipo de Contrataçao', blank=True, null=True, max_length=4, choices=TIPOCONTRATACAO)

    ValorCache = models.DecimalField(
        'Valor', decimal_places=2, max_digits=10, blank=True, null=True)

    Email = models.EmailField(
        'Email do Produtor', blank=True, null=True, max_length=100)
    Telefone = models.CharField(
        'Telefone', blank=True, null=True, max_length=80)
    Celular1 = models.CharField(
        'Celular 1', blank=True, null=True, max_length=80)
    Celular2 = models.CharField(
        'Celular 2', blank=True, null=True, max_length=80)

    Instagram = models.CharField(
        'Instagram', blank=True, null=True, max_length=80)
    Facebook = models.CharField(
        'Facebook', blank=True, null=True, max_length=80)

    Endereco = models.CharField(
        'Endereço', blank=True, null=True, max_length=80)

    Cidade = models.CharField(
        'Cidade', blank=True, null=True, max_length=80)
    UF = models.CharField(
        'Estado', blank=True, null=True, max_length=3, choices=UF)
    CEP = models.IntegerField(
        'CEP', blank=True, null=True)

    Aniversario = models.DateField(
        'Nascimento', blank=True, null=True)

    class Meta:
        """Meta definition for Contratante."""

        verbose_name = 'Produtor'
        verbose_name_plural = 'Produtores'

    def __str__(self):

        return self.Nome


class Tecnico(models.Model):
    """Model definition for Contratante."""

    Nome = models.CharField(
        'Nome do Tecnico', blank=True, null=True, max_length=80)
    DescricaoServico = models.CharField(
        'Descriçao do Serviço', blank=True, null=True, max_length=30, choices=TECNICO)
    Score = models.IntegerField(
        'Score', blank=True, null=True, max_length=3, choices=SCORE)

    TipoContratacao = models.CharField(
        'Tipo de Contratação', blank=True, null=True, max_length=4, choices=TIPOCONTRATACAO)

    ValorCache = models.DecimalField(
        'Valor', decimal_places=2, max_digits=10, blank=True, null=True)

    Email = models.EmailField(
        'Email do Técnico', blank=True, null=True, max_length=100)
    Telefone = models.CharField(
        'Telefone', blank=True, null=True, max_length=80)
    Celular1 = models.CharField(
        'Celular 1', blank=True, null=True, max_length=80)
    Celular2 = models.CharField(
        'Celular 2', blank=True, null=True, max_length=80)

    Instagram = models.CharField(
        'Instagram', blank=True, null=True, max_length=80)
    Facebook = models.CharField(
        'Facebook', blank=True, null=True, max_length=80)

    Endereco = models.CharField(
        'Endereço', blank=True, null=True, max_length=80)

    Cidade = models.CharField(
        'Cidade', blank=True, null=True, max_length=80)
    UF = models.CharField(
        'Estado', blank=True, null=True, max_length=3, choices=UF)
    CEP = models.IntegerField(
        'CEP', blank=True, null=True)

    Aniversario = models.DateField(
        'Nascimento', blank=True, null=True)

    class Meta:
        """Meta definition for Contratante."""

        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'

    def __str__(self):

        return self.Nome


class Staff(models.Model):
    """Model definition for Contratante."""

    Nome = models.CharField(
        'Nome do Tecnico', blank=True, null=True, max_length=80)
    DescricaoServico = models.CharField(
        'Descriçao do Serviço', blank=True, null=True, max_length=30, choices=STAFF)
    Score = models.IntegerField(
        'Score', blank=True, null=True, max_length=3, choices=SCORE)

    TipoContratacao = models.CharField(
        'Tipo de Contrataçao', blank=True, null=True, max_length=4, choices=TIPOCONTRATACAO)

    ValorCache = models.DecimalField(
        'Valor', decimal_places=2, max_digits=10, blank=True, null=True)

    Email = models.EmailField(
        'Email do Musico', blank=True, null=True, max_length=100)
    Telefone = models.CharField(
        'Telefone', blank=True, null=True, max_length=80)
    Celular1 = models.CharField(
        'Celular 1', blank=True, null=True, max_length=80)
    Celular2 = models.CharField(
        'Celular 2', blank=True, null=True, max_length=80)

    Instagram = models.CharField(
        'Instagram', blank=True, null=True, max_length=80)
    Facebook = models.CharField(
        'Facebook', blank=True, null=True, max_length=80)

    Endereco = models.CharField(
        'Endereço', blank=True, null=True, max_length=80)

    Cidade = models.CharField(
        'Cidade', blank=True, null=True, max_length=80)
    UF = models.CharField(
        'Estado', blank=True, null=True, max_length=3, choices=UF)
    CEP = models.IntegerField(
        'CEP', blank=True, null=True)

    Aniversario = models.DateField(
        'Nascimento', blank=True, null=True)

    class Meta:
        """Meta definition for Contratante."""

        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'

    def __str__(self):

        return self.Nome


class Evento(models.Model):
    """Model definition for TipoEvento."""

    NomeEvento = models.CharField(
        'Tipo de Evento', blank=True, null=True, max_length=80)
    CidadeEvento = models.CharField(
        'Cidade do Evento', blank=True, null=True, max_length=80)
    CEPEvento = models.IntegerField(
        'CEP', blank=True, null=True)
    UFEvento = models.CharField(
        'UF do Evento', blank=True, null=True, max_length=3)
    DataEventoInicio = models.DateTimeField(
        'Data Inicial do Evento', blank=True, null=True)
    DataEventoFinal = models.DateTimeField(
        'Data Final do Evento', blank=True, null=True)
    #TipoEvento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for TipoEvento."""

        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.NomeEvento


class Proposta(models.Model):
    """Model definition for TipoEvento."""

    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    PublicoEvento = models.IntegerField(
        'Público do Evento', blank=True, null=True)
    ValorMedioBilhete = models.DecimalField(
        'Valor Médio do Bilhete', max_digits=15, decimal_places=2, blank=True, null=True)
    DataEventoInicio = models.DateTimeField(
        'Data Inicial do Evento', blank=True, null=True)
    DataEventoFinal = models.DateTimeField(
        'Data Final do Evento', blank=True, null=True)

    class Meta:
        """Meta definition for TipoEvento."""

        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'

    def __str__(self):
        return self.Evento
