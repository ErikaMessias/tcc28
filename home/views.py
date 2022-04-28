from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from django.db import connection
import cx_Oracle as Database
from django.shortcuts import render
import cx_Oracle
import math 

def getPagination(request, listItems):
    paginas = math.ceil(listItems.count()/10)
    if 'page' in request.GET:
        try:
            parameter_page = request.GET['page']
            
            if (int(parameter_page) <= 0):
                parameter_page = '1'
            page = Paginator(listItems, 10)
            return [page.page(parameter_page), page.count, page.num_pages]
        except (EmptyPage, PageNotAnInteger):
            return [page.page(1), 0, 0]
    else:
        return [listItems, 0, 0]
# ----------------------------------------------------------------------------------------------
class PesquisaView(APIView):
    """
    API pesquisa
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
            if 'produto_num' in request.GET:            
                produto_num = request.GET['produto_num']
                pesquisa = redlakeSearch_numero(produto_num)
                return Response({"produtos": pesquisa})
            
            elif 'produto_name' in request.GET: 
                produto_name = request.GET['produto_name']
                pesquisa = redlakeSearch_name(produto_name)
                return Response({"produtos": pesquisa})
#-----------------------------------------------------------------------------------------#
def redlakeSearch_numero(produto_num):
    connection = cx_Oracle.connect(user="lge1ca", password="Safira2021!leo",dsn="redlake_dwhp.world")
    cursor = connection.cursor()
    sql = """SELECT MARD.MATNR, MARD.LABST, MAKT.MAKTX FROM INFM_PSLA_CSC2.V_REPL_MARD_B2 MARD inner join INFM_PSLA_CSC2.V_REPL_MAKT_B2 MAKT
    ON MARD.MATNR = MAKT.MATNR where MARD.MATNR = :mid and MARD.WERKS = '908A' and MARD.LABST <> 0"""
    cursor.execute(sql, mid=produto_num)

    return cursor
#-----------------------------------------------------------------------------------------#
def redlakeSearch_name(produto_name):
    produto_name = '%' + produto_name + '%'
    print (produto_name)
    connection = cx_Oracle.connect(user="lge1ca", password="Safira2021!leo",dsn="redlake_dwhp.world")
    cursor = connection.cursor()
    sql = """SELECT MARD.MATNR, MARD.LABST, MAKT.MAKTX FROM INFM_PSLA_CSC2.V_REPL_MARD_B2 MARD inner join INFM_PSLA_CSC2.V_REPL_MAKT_B2 MAKT
    ON MARD.MATNR = MAKT.MATNR where lower(MAKT.MAKTX) like lower(:mid) and MARD.WERKS = '908A' and MARD.LABST <> 0"""
    cursor.execute(sql, mid=produto_name)

    return cursor
# -------------------------------------------------------------------------------------------
class nivelAcessoView(APIView):
    """
    API nivelAcesso
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        # redlakeSearch()
        if 'nivel' in request.GET:            
            nivel = request.GET['nivel']
            Acesso = nivelAcesso.objects.filter(id=nivel)
            serializer = nivelAcessoSerializer(Acesso, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            Acesso = nivelAcesso.objects.get(id=pk)
            serializer = nivelAcessoSerializer(Acesso)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            Acesso = nivelAcesso.objects.all()
            serializer = nivelAcessoSerializer(Acesso, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = nivelAcessoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        Acesso = nivelAcesso.objects.get(id=pk)
        serializer = nivelAcessoSerializer(Acesso, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        Acesso = nivelAcesso.objects.get(id=pk)
        Acesso.delete()
        return Response({"msg": "Apagado com sucesso"})
#-----------------------------------------------------------------------------------------#
class ResponsavelView(APIView):
    """
    API Responsavel
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'respon' in request.GET:
            respon = request.GET['respon']
            dado = Responsavel.objects.filter(id=respon)
            serializer = ResponsavelSerializer(dado, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dado = Responsavel.objects.get(id=pk)
            serializer = ResponsavelSerializer(dado)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            dado = Responsavel.objects.all()
            serializer = ResponsavelSerializer(dado, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = ResponsavelSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        dado = Responsavel.objects.get(id=pk)
        serializer = ResponsavelSerializer(dado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dado = Responsavel.objects.get(id=pk)
        dado.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class ProdutoView(APIView):
    """
    API Produto
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'prod' in request.GET:
            prod = request.GET['prod']
            dad = Produto.objects.filter(id=prod)
            serializer = ProdutoSerializer(dad, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dad = Produto.objects.get(id=pk)
            serializer = ProdutoSerializer(dad)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            dad = Produto.objects.all()
            serializer = ProdutoSerializer(dad, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        dad = Produto.objects.get(id=pk)
        serializer = ProdutoSerializer(dad, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dad = Produto.objects.get(id=pk)
        dad.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class TransacaoSucataView(APIView):
    """
    API TransacaoSucata
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'id' in request.GET:
            id = request.GET['id']
            base = TransacaoSucata.objects.filter(id_user=id)
            serializer = TransacaoSucataSerializerRead(base, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        
        elif pk != '':
            infoss = TransacaoSucata.objects.get(id=pk)
            serializer = TransacaoSucataSerializerRead(infoss)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            infoss = TransacaoSucata.objects.all()
            serializer = TransacaoSucataSerializerRead(infoss, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = TransacaoSucataSerializerRead(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        infoss = TransacaoSucata.objects.get(id=pk)
        serializer = TransacaoSucataSerializerRead(infoss, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        infoss = TransacaoSucata.objects.get(id=pk)
        infoss.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class TransacaoProdutoView(APIView):
    """
    API TransacaoProduto
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'id_user' in request.GET:
            id_user = request.GET['id_user']
            base = TransacaoProduto.objects.filter(id_user_Salva=id_user)
            serializer = TransacaoProdutoSerializer(base, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        
        elif pk != '':
            base = TransacaoProduto.objects.get(id=pk)
            serializer = TransacaoProdutoSerializer(base)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            base = TransacaoProduto.objects.all()
            serializer = TransacaoProdutoSerializer(base, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = TransacaoProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        base = TransacaoProduto.objects.get(id=pk)
        serializer = TransacaoProdutoSerializer(base, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        base = TransacaoProduto.objects.get(id=pk)
        base.delete()
        return Response({"msg": "Apagado com sucesso"})
#-----------------------------------------------------------------------
class UsuarioAPIView(APIView):
    """
    API Usuario
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'user' in request.GET:
            user = request.GET['user']
            usuarios = Usuario.objects.filter(user=user)
            serializer = UsuarioSerializer(usuarios, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )            
        elif pk == '':
            usuarios = Usuario.objects.all()
            resp = getPagination(request, usuarios)
            serializer = UsuarioSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        else:
            usuarios = Usuario.objects.get(idUserFK=pk)
            serializer = UsuarioSerializer(usuarios)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )


    def post(self, request):        
        serializer = UsuarioSerializer(data=request.data, many=True)      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        usuarios = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        usuarios = Usuario.objects.get(id=pk)
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})

# ---------------------------------------------------------------------#
class CentralTrabView(APIView):
    """
    API CentralTrab
    """
    def get(self, request, pk=''):
            Acesso = CentralTrab.objects.all()
            resp = getPagination(request, Acesso)   
            serializer = CentralTrabSerializer(resp[0], many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2],

                    "msg": "sucesso"
                }
            )
# -------------------------------------------------------------------------------------

    

