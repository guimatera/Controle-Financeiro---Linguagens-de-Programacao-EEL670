from bs4 import BeautifulSoup
from urllib.request import urlopen
import yfinance as yf


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
   
class dolar_cambio():
    def __init__(self):
        self.ticker = yf.Ticker('USDBRL=X')
    
    def get_dolar(self): 
        ticker = self.ticker.history(period='1d', interval='1m')
        return float(ticker['Close'].iloc[-1])


class euro_cambio():
    def __init__(self):
        self.ticker = yf.Ticker('EURBRL=X')
    
    def get_euro(self): 
        ticker = self.ticker.history(period='1d', interval='1m')
        return float(ticker['Close'].iloc[-1])


class bitcoin(dolar_cambio):
    def __init__(self):
        super().__init__()
        self.bit_ticker_dolar = yf.Ticker('BTC-USD')

    def get_bitcoin_dolar(self):
        b_ticker = self.bit_ticker_dolar.history(period='1d', interval='1m')
        return float(b_ticker['Open'].iloc[-1])
    
    def get_bitcoin_real(self):
        b_ticker = self.bit_ticker_dolar.history(period='1d', interval='1m')
        a = dolar_cambio()
        return float(b_ticker['Open'].iloc[-1] * a.get_dolar()) 

 
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
