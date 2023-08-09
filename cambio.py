import requests
import json
import datetime
from twilio.rest import Client


######################################## COTAÇAO DO EURO EM TEMPO REAL ENVIADO POR SMS TODOS OS DIAS MESMO COM O COMPUTADOR DESLIGADO.

data_atual = datetime.date.today()

cotacao = requests.get('https://economia.awesomeapi.com.br/json/last/EUR-BRL') ##CASO QUEIRA MUDAR A MOEDA É SÓ PEGAR O CÓDIGO NA API DA AWESOMEAPI
cotacao_dic = cotacao.json()
euro2casas = float(cotacao_dic['EURBRL']['bid'])

print('\nOlá \nHoje, {} \nA cotação do Euro esta: R${:.2f}\nVerifique as altas e baixas para realizar suas compras no cartão de crédito!'.format(data_atual, euro2casas)) ##ver a mensagem que foi enviada


from twilio.rest import Client

account_sid = 'seuid'
auth_token = 'seutoken'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='numero registrado no twilio',
  body=('\nOlá \nHoje, {} \nA cotação do Euro esta: R${:.2f}\nVerifique as altas e baixas para realizar suas compras no cartão de crédito!'.format(data_atual, euro2casas)),
  to='numero verificado no twilio',
)

print(message.sid)

