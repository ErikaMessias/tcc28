from rest_framework import serializers
from .models import *
from rest_framework import viewsets

# -------------------------------------------------------------------------
class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'
class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
# -------------------------------------------------------------------------
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
# -------------------------------------------------------------------------

class CentralTrabSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralTrab
        fields = '__all__'
class CentralTrabViewSet(viewsets.ModelViewSet):
    queryset = CentralTrab.objects.all()
    serializer_class = CentralTrabSerializer
# -------------------------------------------------------------------------
    
class nivelAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = nivelAcesso
        fields = '__all__'
# -------------------------------------------------------------------------
class TransacaoSucataSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = TransacaoSucata
        fields = '__all__'
# -------------------------------------------------------------------------
class TransacaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransacaoProduto
        fields = '__all__'
class TransacaoProdutoViewSet(viewsets.ModelViewSet):
    queryset = TransacaoProduto.objects.all()
    serializer_class = TransacaoProdutoSerializer
# -------------------------------------------------------------------------
class UsuarioSerializer(serializers.ModelSerializer):
    idNivelAcessFK = nivelAcessoSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
# -------------------------------------------------------------------------


