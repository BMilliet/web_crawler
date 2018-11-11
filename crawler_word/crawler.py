
"""
   Este é um crawler feito em Python3 utilizando BeautifulSoup.
   Sua funcionalidade se resume a seguir uma lista de URLs,
   em busca de uma palavra definida pelo usuario,
   após a busca exibe um relatório com os resultados.
   O programa busca por um arquivo de texto contendo as URLs,
   por padrão o nome do arquivo procurado é 'URL_list.txt'.
   Os resultados são disponibilizados em formato JSON.

"""

import urllib.request
import json
from bs4 import BeautifulSoup
from bs4.element import Comment



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



"""Seleciona o conteudo a ser ignorado"""

def valida_tag(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    else:
        return True



"""Extrai o conteudo ignorado"""

def limpa_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visivel = filter(valida_tag, texts)
    return u" ".join(t.strip() for t in visivel)



"""Le o HTML selecionando apenas oque deve ser lido e conta a ocorrencia da palavra"""

def conta_palavra(urls,palavra):
    results = []

    for i in range(len(urls)-1):
        resp = urllib.request.urlopen(urls[i])

        codigo = resp.code
        data = resp.read()
        html = limpa_html(data)
        cont = html.count(palavra)

        result = json.dumps({'encontradas': cont, 'codigo': codigo, 'Url': urls[i]})
        results.append(result)

    return results



"""Devolver os resultados obtidos em JSON"""

def apresenta_relatorio(results):
    for i in range(len(results)):
        resp = json.loads(results[i])
        print(resp)



"""Execução do programa"""

urls = busca_lista('URL_list.txt')



"""A palavra buscada é colocada como um input pelo usuario ao executar o programa"""

palavra = input('Qual palavra deseja procurar? ');

results = conta_palavra(urls,palavra)
apresenta_relatorio(results)

print('Fim')
