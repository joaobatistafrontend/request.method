from ctypes.wintypes import PINT
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print('path')
    print(request.path) # pagina da requisição

    print('method')
    print(request.method) # metodo da requisição
    # if request.method == 'GET':
    #     return HttpResponse('foi um get')
    print('get')
    print(request.GET)
    # 127.0.0.1:8000/?nome=joao&idade=22 ou 127.0.0.1:8000/?nome=joao&idade=22
    #  <QueryDict: {'nome': ['joao'], 'idade': ['22']}>  <QueryDict: {'nome': ['joao', 'batista'], 'idade': ['22']}>
    print('GET.get sem o parametro certo')
    print(request.GET.get('cidade'))

    print('GET.get com um dos parametros')
    print(request.GET.get('nome'))

    print('GET.get com os parametros em lista')
    print(request.GET.getlist('nome'))

    print('META[HTTP)HOST]')
    print(request.META['HTTP_HOST']) #endereço do host utilizado do usuário

    print('META[QUERY_STRING]')
    print(request.META['QUERY_STRING'])
    
    print('ip')
    print(request.META['REMOTE_ADDR'])

    print('porta do servdor')
    print(request.META['SERVER_PORT'])
    
    print('path + query_string')
    print(request.get_full_path)


    print('seguro?')
    print(request.is_secure())
    return HttpResponse('test')