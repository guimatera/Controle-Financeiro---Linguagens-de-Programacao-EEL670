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


class consultor_acao():

    def __init__(self, nome_acao):
        self.nome_acao = nome_acao
        self.sufixo = '.SA'
        self.acao = yf.Ticker(self.nome_acao.upper()+self.sufixo)
        self.ticker = yf.Ticker(self.nome_acao.upper()+self.sufixo)
        self.temas = ['longName','sector','Volume','averageVolume10days','averageVolume',
         'fiveYearAvgDividendYield','dividendYield','open','Close','dayHigh',
         'dayLow','fiftyTwoWeekHigh','fiftyTwoWeekLow','52WeekChange','profitMargins']

    def get_parameters(self):
        basico = ['Nome Completo:', 'Setor:']
        liquidez = ['Volume médio(último dia - R$):', 'Volume médio(últimos 10 dias - R$):', 'Volume médio(últimos 3 meses - R$):']
        dividendos = ['Dividendos(últimos 5 anos - %):', 'Dividendos(último ano - %):']
        preco = ['Preço de abertura(R$):', 'Preço Atual(R$):', 'Máxima do dia(R$):',
        'Mínima do dia(R$):', 'Máxima do ano(R$):', 'Mínima do ano(R$):', 'Variação do ano(%):']
        lucro = ['Margem de Lucro(último ano - %):']
        lista = basico + liquidez + dividendos + preco + lucro
        return lista

    def get_data(self):
        
        dados = []
        ticker = self.ticker.history(period='1d', interval='1d')
        acao = self.acao.info

        for dado in self.temas:
            if dado != 'Close' and dado != 'Volume':
                try:
                    if acao[dado] == 0 or str(acao[dado]) == 'None':
                        dados.append('Sem dados')
                    elif dado == 'fiveYearAvgDividendYield':
                        dados.append(str(acao[dado]) + '%')
                    elif float(acao[dado]) <= 1:
                        valor = round(float(acao[dado]*100),2)
                        dados.append(str(valor)+ '%')
                    else:
                        dados.append(round(float(acao[dado]),2))
                except:
                    dados.append(acao[dado])
            else:
                if float(ticker[dado].iloc[-1]) == 0:
                    dados.append('Sem dados')
                elif float(ticker[dado].iloc[-1]) <= 1:
                    valor = round(float(ticker[dado].iloc[-1]*100),2)
                    dados.append(str(valor)+ '%')
                else:
                    dados.append(round(float(ticker[dado].iloc[-1]),2))
        return dados