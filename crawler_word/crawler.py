import urllib.request
import json

with open('URL_list.txt') as file:
    urls = file.read().split('\n')

palavra = ''

results = []
for i in range(len(urls)-1):
    resp = urllib.request.urlopen(urls[i])
    codigo = resp.code
    data = resp.read()
    html = data.decode("UTF-8")
    cont = html.count(palavra)

    result = json.dumps({'Url': urls[i], 'codigo': codigo, 'encontradas': cont})
    results.append(result)


for i in range(len(results)):
    resp = json.loads(results[i])
    print(resp['encontradas'])
