#url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
import re


class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self._url)

    def __str__(self):
        return self._url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self._url)

        if not match:
            raise ValueError("A url não é valida")

    def get_url_base(self):
        indice_interrogacao = self._url.find('?')
        url_base = self._url[:indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_interrogacao = self._url.find('?')
        url_parametros = self._url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        parametro_busca = 'quantidade'
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor


class Cambio:
    def __init__(self, moeda_destino, valor_origem, cotacao_moeda):
        self.__quantia_moeda = valor_origem
        self.__lastro = moeda_destino
        self.__cotacao_lastro = cotacao_moeda

    def cambio(self):
        return float(self.__quantia_moeda) * self.__cotacao_lastro

    def __str__(self):
        return f'{self.__lastro} {self.cambio()}'


estrator_url = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = estrator_url.get_valor_parametro("quantidade")
moeda_dest = estrator_url.get_valor_parametro("moedaDestino")
parametros_cambio = Cambio(moeda_dest, valor_quantidade, 5.41)
#print(parametros_cambio.cambio())
print(parametros_cambio)
#print(valor_quantidade)
