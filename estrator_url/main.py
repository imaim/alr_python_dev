# "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]

parametro_busca = "moedaDestino"
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
teste = url_parametro.split(sep='&')
teste_dict = {}
count = 0
for i in teste:
    teste_dict[i.split(sep="=")[0]] = i.split(sep="=")[1]
    count += 1
valor = url_parametro[indice_valor:]
print(valor)
print(teste_dict['moedaOrigem'])
