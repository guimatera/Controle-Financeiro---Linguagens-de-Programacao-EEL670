from bs4 import BeautifulSoup
from urllib.request import urlopen
import yfinance as yf
import investpy as inv
from datetime import datetime 


class poupanca():
    def __init__(self, page_poupanca = 'https://www4.bcb.gov.br/pec/poupanca/poupanca.asp?frame=1'):
        self.page_poupanca = page_poupanca
   
    def get_poupanca(self):
        html = urlopen(self.page_poupanca)
        soup = BeautifulSoup(html.read(), 'html.parser')
        linhas = [text for text in soup.stripped_strings]
        valor = str(linhas[-4])[:-1]
        return 1+float(valor.replace(',','.'))/100


class fundos():

    def __init__(self):
        self.data_atual = datetime.today()
        self.ifix = inv.get_index_historical_data('BM&FBOVESPA Real Estate IFIX', country='brazil',
                                                from_date=self.data_atual.strftime('%d/%m/2020'),
                                                 to_date=self.data_atual.strftime('%d/%m/%Y'))
    
    def get_fundos(self): 
        diff = (float(self.ifix['Close'].iloc[-1]) - float(self.ifix['Close'].iloc[0]))/float(self.ifix['Close'].iloc[0])
        return pow(1+diff,1/12)


class acoes():
    def __init__(self):
        self.ticker = yf.Ticker('^BVSP')
    
    def get_acoes(self): 
        ticker = self.ticker.history(period='1y', interval='1d')
        diff = (float(ticker['Close'].iloc[-1]) - float(ticker['Close'].iloc[0]))/float(ticker['Close'].iloc[0])
        return pow(1+diff,1/12)


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

