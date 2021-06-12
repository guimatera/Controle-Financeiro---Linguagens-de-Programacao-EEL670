# Controle-Financeiro---Linguagens-de-Programacao-EEL670

Controle Financeiro é um aplicação web criada para trabalho final da disciplina Linguagens de Programação da UFRJ.

A ideia por trás do projeto é levar ao usuário uma ferramenta que tem como prioridade ajudá-lo a decidir qual o melhor tipo de
investimento que este pode realizar para obter melhores rendimentos financeiros no futuro.

A aplicação possui funcionalidades básicas como cadastro de usuários novos, login de usuários que já possuem conta no site e 
logout para sair da homepage uma vez logado no site. Vale ressaltar que todos os dados são armazenados num banco de dados programado 
com a tecnologia do SQLalchemy.

As funcionalidades que fazem jus ao nome 'Controle Financeiro' são as seguintes:
(Só é possível fazer uso dessas funconalidades quando logado no site)

- Conversor Dólar-Real: Uma calculadora que, a partir de dados da taxa de câmbio dólar-real em tempo real, converte um montante em reais
para dólar. A conversão inversa também é realizada.

- Conversor Euro-Real: Uma calculadora que, a partir de dados da taxa de câmbio euro-real em tempo real, converte um montante em reais
para euro. A conversão inversa também é realizada.

- Calculadora de Bitcoins: Uma calculadora que, a partir de dados da taxa de câmbio real-BTC e dólar-BTC em tempo real, converte um montante em reais ou dólares
para a criptomoeda Bitcoin. As conversões inversas também são realizadas.

- Calculadora de Investimentos: Uma calculadora que realiza a previsão de quanto um investidor irá faturar caso invista em um determinado setor de investimentos. 
Os dados disponíveis nessa calculadora são: IBOV(mercado de ações), IFIX(fundos imobiliários) e poupança, todos atualizados em tempo real. Com essa funcionalidade,
o usuário, apenas informando o montante, aporte mensal e período de investimento, pode comparar qual é o melhor retorno em termos financeiros dentre os setores analisados.

- Consultor de Ações: Uma funcionaldade onde o usuário, apenas informando o código de uma ação brasileira presente no mercado de ações, tem acesso a diversas informações
sobre ela, como, por exemplo, a liquidez da ação, a taxa de dividendos paga pela empresa, o lucro da empresa, entre outras informações relevantes para se fazer uam análise 
segura de invetimento no mercado de ações.

Nessas funcionalidades, foram utilizadas API's de mercado financeiro com o Python, como yfinance e Investpy (dados de IFIX) para obter, a partir da internet, dados que
foram utilizados nas calculadoras e consultores. O Beautiful Soup também foi implementado para buscar dados da taxa de rendimento de poupança.

Em geral, utilizamos CSS e bootstrap para o embelezamento do site, Javascript para criar as colculadoras e adicionar data e hora atuais na homepage do usuário, Python para
implementar uma estruturação de código MVC, buscar dados da internet e implementar um banco de dados. 

Para rodar  o programa, basta escrever no terminal do Vscode 'python run.py runserver'.




