
"""
   Este é um crawler feito em Python3
   Sua funcionalidade se resume a seguir uma lista de URLs,
   em busca de uma palavra definida pelo usuario,
   após a busca exibe um relatório com os resultados.
   O programa busca por um arquivo de texto contendo as URLs,
   por padrão o nome do arquivo procurado é 'URL_list.txt'.
   Os resultados são disponibilizados em formato JSON.

"""

import urllib.request
import urllib.error
import json

"""
    A definição padrão para se diferenciar as URLs é uma quebra de linha,
    as URLs deve estar colocadas uma em cada linha.
"""

fileFound = False
try:
    lista = open('URL_list.txt')
    try:
        urls = lista.read().split('\n')
        fileFound = True
    finally: lista.close()

except FileNotFoundError:
        print('Arquivo de lista não encontrado')


"""A palavra buscada é colocada como um input pelo usuario ao executar o programa"""

if(fileFound):
    palavra = input('Qual palavra deseja procurar? ');
    results = []

    for i in range(len(urls)-1):
        resp = urllib.request.urlopen(urls[i])

        codigo = resp.code
        data = resp.read()
        html = data.decode("UTF-8")
        cont = html.count(palavra)
        result = json.dumps({'Url': urls[i], 'codigo': codigo, 'encontradas': cont})
        results.append(result)


"""
   Os resultados contem a URL, o codigo de resposta e o numero de palavras encontradas
"""
    for i in range(len(results)):
        resp = json.loads(results[i])
        print(resp['encontradas'])


print('\nFim')
