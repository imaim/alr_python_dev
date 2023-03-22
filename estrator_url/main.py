# "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "bytebank.com/cambio?moedaOrigem=real"
url_base = url[0:19]
url_parametro = url[20:36]
print(url_parametro)