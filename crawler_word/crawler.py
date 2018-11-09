
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
import json

"""
    A definição padrão para se diferenciar as URLs é uma quebra de linha,
    as URLs deve estar colocadas uma em cada linha.
"""

def busca_lista(list):
    try:
        lista = open(list)
        try:
            urls = lista.read().split('\n')
        finally: lista.close()

    except FileNotFoundError:
        print('Arquivo de lista não encontrado')

    return urls


def conta_palavra(urls,palavra):
    results = []

    for i in range(len(urls)-1):
        resp = urllib.request.urlopen(urls[i])

        codigo = resp.code
        data = resp.read()
        html = data.decode("UTF-8")
        cont = html.count(palavra)

        result = json.dumps({'Url': urls[i], 'codigo': codigo, 'encontradas': cont})
        results.append(result)

    return results


def apresenta_relatorio(results):
    for i in range(len(results)):
        resp = json.loads(results[i])
        print(resp['encontradas'])

"""Execução do programa"""

urls = busca_lista('URL_list.txt')

"""A palavra buscada é colocada como um input pelo usuario ao executar o programa"""

palavra = input('Qual palavra deseja procurar? ');

results = conta_palavra(urls,palavra)
apresenta_relatorio(results)

print('Fim')
