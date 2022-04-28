from statistics import mode
from unicodedata import decimal
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def upload_image_produto(instance, filename):
    return f"{instance.partNumber}-{timezone.now()}-{filename}"

class centroCusto(models.Model):
    codigoCentro = models.CharField(max_length=20)

    def __str__(self):
        return self.codigoCentro

class tipoMovimento(models.Model):
    nometipoMovimento = models.CharField(max_length=20)

    def __str__(self):
        return self.nometipoMovimento
    
class contaRazao(models.Model):
    nomeContaRazao = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeContaRazao

class tipoOrdem(models.Model):
    nomeTipoOrdem = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeTipoOrdem
    
class prioridade(models.Model):
    nomePrioridade = models.CharField(max_length=20)

    def __str__(self):
        return self.nomePrioridade
    
class localInstal(models.Model):
    nomeLocalInstal = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeLocalInstal

class tipoAtv(models.Model):
    nometipoAtv = models.CharField(max_length=20)

    def __str__(self):
        return self.nometipoAtv

class CentralTrab(models.Model):
    nomeCentralTrab = models.CharField(max_length=20)
    den = models.CharField(max_length=100, blank=True)
    des = models.CharField(max_length=100, blank=True)
    ex = models.CharField(max_length=100, blank=True)
    ori = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nomeCentralTrab

class Responsavel(models.Model):
    nomeResponsavel = models.CharField(max_length=20)
    email_resp = models.EmailField()

    def __str__(self):
        return self.nomeResponsavel

class Produto(models.Model):
    nomeProduto = models.CharField(max_length=20)
    partNumber = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_produto,height_field=None, width_field=None, blank=True, null=True)

    def __str__(self):
        return self.nomeProduto

class nivelAcesso(models.Model):
    nomeAcesso = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeAcesso

class divisao(models.Model):
    nomeDivisao = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeDivisao

class TransacaoSucata(models.Model):
    desc = models.CharField(max_length=100)
    txtBreve = models.CharField(max_length=20)
    trab  = models.DecimalField(max_digits=5, decimal_places=2)
    dataInser = models.DateField(default=timezone.now)
    user = models.CharField(blank=True, default="", max_length=15)
    id_user = models.CharField(blank=True, default="", max_length=5)
    un = models.CharField(max_length=2, blank=True, null=True, default="H")
    idtipoOrdemFK = models.ForeignKey(tipoOrdem, related_name="tipo_ordem", blank=True, null=True, default="1", on_delete=models.CASCADE)
    idLocalFK = models.ForeignKey(localInstal, related_name="localInstal", blank=True, null=True, default="1", on_delete=models.CASCADE)
    idtipoavtFK = models.ForeignKey(tipoAtv, related_name="tipoAtv", blank=True, null=True, default="1", on_delete=models.CASCADE)
    idCenTrabFK = models.ForeignKey(CentralTrab, related_name="CentralTrab", blank=True, null=True, default="1", on_delete=models.CASCADE)
    iddivisaoFK = models.ForeignKey(divisao, related_name="divisao", blank=True, null=True, default="1", on_delete=models.CASCADE)
    idCentroCustoFK = models.ForeignKey(centroCusto, related_name="centroCusto", blank=True, null=True, default="1", on_delete=models.CASCADE)

    def __str__(self):
        return self.desc

class TransacaoProduto(models.Model):
    idCentroCFK = models.ForeignKey(centroCusto, blank=True, null=True, on_delete=models.CASCADE)
    idTipoMovimentoFK = models.ForeignKey(tipoMovimento, blank=True, null=True, on_delete=models.CASCADE)
    idContaRazaoFK = models.ForeignKey(contaRazao, blank=True, null=True, on_delete=models.CASCADE)
    user_Salva = models.CharField(blank=True, default="", max_length=15)
    id_user_Salva= models.CharField(blank=True, default="", max_length=5)
    recebedor = models.CharField(max_length=15)
    codigo = models.CharField(blank=True, max_length=15)
    material = models.CharField(max_length=50)
    dataIInsercao = models.DateField(default=timezone.now)
    quantidade = models.IntegerField()
    umr = models.CharField(max_length=10, blank=False, null=False)
    dep = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.material

class Usuario(models.Model):
    edv = models.BigIntegerField()
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    idUserFK = models.ForeignKey(User, on_delete=models.CASCADE)
    idRespFK = models.ForeignKey(Responsavel, blank=True, null=True, on_delete=models.CASCADE)
    idNivelAcessFK = models.ForeignKey(nivelAcesso, blank=True, null=True, on_delete=models.CASCADE)








