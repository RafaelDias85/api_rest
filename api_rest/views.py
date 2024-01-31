from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuarios
from .serializers import UsuariosSerializers

import json

@api_view(['GET'])
def get_usuarios(request):

    if request.method == 'GET':

        usuarios = Usuarios.objects.all() #Get all objects in usuarios database (it returns a queryset)
                                          #Obter todos os objetos no banco de dados 'usuarios' (isso retorna um conjunto de consultas).
        
        serialiser = UsuariosSerializers( usuarios, many=True) #Serialize the object data into json (has a 'many' parameter cause it's a queryset)
                                                               #"Serializar os dados do objeto em JSON (tem um parâmetro 'many' porque é um conjunto de consultas)."
        return Response (serialiser.data) #return the serialized data
                                          #Retornar os dados serializados.
    
    return Response (status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_by_nick(request, nick):

    try:
        usuario = Usuarios.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsuariosSerializers(usuario)
        return Response (serializer.data)
    

#Crud
@api_view (['GET','POST','PUT','DELETE'])
def  gerencia_usuario(request):
    if request.method =='GET':
        try:
            if request.GET['Usuarios']:
                usuario_nickname = request.GET['Usuarios']
                usuario = Usuarios.objects.get(pk=usuario_nickname)
                serializer = UsuariosSerializers(usuario)
                return Response(serializer.data)
            else:    
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

#https://www.youtube.com/watch?v=Q2tEqNfgIXM