from unicodedata import decimal

from django.db import models
from math import ceil

class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.CharField(max_length=100, blank=True, null=True,verbose_name='Endereço')
    complemento = models.CharField(max_length=50, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    fone = models.CharField(max_length=20, blank=True, null=True, verbose_name= 'Telefone')
    email = models.EmailField(verbose_name='E-mail')
    foto = models.ImageField(upload_to='cliente_foto', blank=True, null=True, verbose_name='')

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Marca')
    url = models.URLField(verbose_name='Site', blank=True, null=True)
    logo = models.ImageField(upload_to='marca_logo', blank=True, null=True, verbose_name='')

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=8, verbose_name='Placa')
    modelo = models.CharField(max_length=30, blank=True, null=True, verbose_name='Modelo')
    cor = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cor')
    marca_id = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Fabricante')
    ano = models.IntegerField(default=2023, blank=True, null=True, verbose_name='Ano' )
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    foto = models.ImageField(upload_to='veiculo_foto', blank=True, null=True, verbose_name='')

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

    class Meta:
        verbose_name_plural = 'Veículos'


class Tabela(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor')

    def __str__(self):
        return f'{self.descricao} - {self.valor}'

    class Meta:
        verbose_name_plural = 'Tabelas'


class Mensalista(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veículo')
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Valor')
    observacoes = models.TextField(blank=True, null=True, verbose_name="Obs.")

    class Meta:
        verbose_name_plural = "Mensalistas"

    def __str__(self):
        return self.id_veiculo


class Rotativo(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veículo')
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Valor')
    entrada = models.DateTimeField(auto_now=False, verbose_name='Entrada')
    saida = models.DateTimeField(auto_now=False, blank=True, null=True, verbose_name='Saída')
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,verbose_name='Total')
    pago = models.BooleanField(default=False, verbose_name='Pago')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Obs.')

    class Meta:
        verbose_name_plural = 'Rotativos'

    def __str__(self):
        return f'{self.id_veiculo} - {self.id_tabela}'

    def calcula_total(self):
        if self.saida:
            hora = ((self.saida - self.entrada ).total_seconds()/3600)
            obj = Tabela.objects.get(id= self.id_tabela.pk)
            if hora <= 0.5:
                self.total = float(obj.valor) / 2.0
            else:
                self.total = ceil(hora) * float(obj.valor)
            return self.total
        return 0.0