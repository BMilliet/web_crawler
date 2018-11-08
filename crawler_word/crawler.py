import urllib.request
import json

urls = []
palavra = ''

results = []
for i in range(len(urls)):
    resp = urllib.request.urlopen(urls[i])
    codigo = resp.code
    data = resp.read()
    html = data.decode("UTF-8")
    cont = html.count(palavra)

    result = json.dumps({'Url': urls[i], 'codigo': codigo, 'encontradas': cont})
    results.append(result)


for i in range(len(urls)):
    resp = json.loads(results[i])
    print(resp['encontradas'])
