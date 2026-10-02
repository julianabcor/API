#UMA API É UM JEITO DE CONECTAR SISTEMAS, INTERFACE DE PROGRAMAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E APLICAÇÕES E PADRÕES QUE PERMITE QUE DFEREENTES SISTEMAS
#DE SOFTWERE DE COMUNICAÇÃO SE COMUNIQUEM
#NESTE EXEPLO SERA UTLIZADA A WEATHERAPI.COM PARA CONSULTAR AS CONDIÇÕES
#CLIMÁTICAS DE UMA DETERMINDADA LOCALIDADE;
#CONSUMIR API->
#VAMOS PRECISAR DE UM PROGRAMA QUE TENHA UM CERTA CAPACIDADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA
#VAMOS PRECISAR DE UMA APIKEY -> UMA CREDENCIAL 

import requests #biblibioteca para fazer requisições http
from pprint import pprint #biblioteca para imprimir os dados de forma legível

link_API = 'http://api.weatherapi.com/v1/current.json'
link_API2 = 'http://api.weatherapi.com/v1/timezone.json'

cid = input('Digite a cidade que você quer saber a temperatura:')
cid2 = input('Digite o país que você quer saber o fuso horário:')

parametros = {
    'key': API_CHAVE,
    'q': cid, #cidade para qual queremos obter os dados
    'lang':"pt" #linguagem
}

parametros2 = {
    'key': API_CHAVE,
    'q': cid2 #país para qual queremos obter o fuso horário
}

#Armazenando a resposta da requisição da variavel resposta
resposta = requests.get(link_API, params = parametros)
resposta2 = requests.get(link_API2, params = parametros2)

#print(resposta)
print(resposta.text)

if resposta.status_code == 200:
    print('Requisição realizada com sucesso!')
    dados = resposta.json() #armazenando os dados em formato json na variavel dados
    #pprint(dados)
    temp = dados['current']['temp_c']#armazenando a temperatura C°
    descri = dados['current']['condition']['text']#armazenando a descrição
    print('A temperatura atual na cidade escolhida é de: {}'.format(temp))
    print('Descrição do clima: {}'.format(descri))

else:
    print("Erro na requisição.")

if resposta2.status_code == 200:
    dados2 = resposta2.json()
    fuso = dados2['location']['tz_id']
    print('O fuso horário do país escolhido é: {}'.format(fuso))

else:
    print("Erro na requisição do fuso horário.")