from bs4 import BeautifulSoup
from urllib.request import urlopen


class poupanca():
    def __init__(self, page_poupanca = 'http://www.idealsoftwares.com.br/indices/poupanca2021.html'):
        self.page_poupanca = page_poupanca
   
    def get_poupanca(self):
        html = urlopen(self.page_poupanca)
        soup = BeautifulSoup(html.read(), 'html.parser')
        linhas = [text for text in soup.stripped_strings]
        valor = str(linhas[7])[:-1]
        return 1+float(valor.replace(',','.'))/100


class fundos():
    def __init__(self, page_fundos = 'https://www.infomoney.com.br/cotacoes/ifix/'):
        self.page_fundos = page_fundos
   
    def get_fundos(self):
        html = urlopen(self.page_fundos)
        soup = BeautifulSoup(html.read(), 'html.parser')
        linhas = [text for text in soup.stripped_strings]
        num = linhas.index('Variação (52 semanas)')
        valor = str(linhas[num+1])[:-1]
        if float(valor) > 0:
            valor = 1+float(valor)/100
            return pow(valor,1/12)
        else: 
            valor = -1+float(valor)/100
            return pow(valor,1/12)
   
'''
class cripto():
    def __init__(self, page_cripto = 'https://www.infomoney.com.br/cotacoes/bitcoin-btc/'):
        self.page_cripto = page_cripto
   
    def get_cripto(self):
        html = urlopen(self.page_cripto)
        soup = BeautifulSoup(html.read(), 'html.parser')
        linhas = [text for text in soup.stripped_strings]
        valor = str(linhas[189])[:-1]
        if float(valor) > 0:
            return 1+float(valor)/100
        else: 
            return -1+float(valor)/100
'''

 
class acoes():
    def __init__(self, page_acoes = 'https://www.infomoney.com.br/cotacoes/ibovespa/'):
        self.page_acoes = page_acoes
   
    def get_acoes(self):
        html = urlopen(self.page_acoes)
        soup = BeautifulSoup(html.read(), 'html.parser')
        linhas = [text for text in soup.stripped_strings]
        num = linhas.index('Variação (52 semanas)')
        valor = str(linhas[num+1])[:-1]
        if float(valor) > 0:
            valor = 1+float(valor)/100
            return pow(valor,1/12)
        else: 
            valor = -1+float(valor)/100
            return pow(valor,1/12)


class dolar_cambio():
    def __init__(self, page_dolar = 'https://www.infomoney.com.br/ferramentas/cambio/'):
        self.page_dolar = page_dolar
   
    def get_dolar(self):
        html = urlopen(self.page_dolar)
        soup = BeautifulSoup(html.read(), 'html.parser')
        linhas = [text for text in soup.stripped_strings]
        num = linhas.index('Dólar Comercial')
        valor = str(linhas[num+1])
        return float(valor.replace(',','.'))


class euro_cambio():
    def __init__(self, page_euro = 'https://www.infomoney.com.br/ferramentas/cambio/'):
        self.page_euro = page_euro
   
    def get_euro(self):
        html = urlopen(self.page_euro)
        soup = BeautifulSoup(html.read(), 'html.parser')
        linhas = [text for text in soup.stripped_strings]
        num = linhas.index('Euro')
        valor = str(linhas[num+1])
        return float(valor.replace(',','.'))


        