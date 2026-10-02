# Uma API é um jeito de conectar sistemas, interface de programação e aplicações;
# API é um conjunto de regras e padrões que permite que diferentes sistemas de software se comuniquem e troquem dados entre si 

# Neste exemplo, será utilizada a "weatherapi.com" para consultar as condições climáticas de uma determinada localidade;

# Consumir API ->
# Vamos precisar de um programa que tenha uma certa capacidade de pegar dados mediante a uma URL pré definida

import requests   # Biblioteca para fazer requisições HTTP
from pprint import pprint   # Biblioteca para imprimir os dados de forma legível

# Vamos precisar da APIKEY -> uma credencial


API_link = "http://api.weatherapi.com/v1/sports.json"

escolha = input("Escolha a cidade que deseja ver o clima: ")

parametros = {
    "key": API_key,
    "q": escolha, # Cidade para qual queremos obter os dados
    "lang":"fr" # Linguagem
}
# Armazenando a resposta da requisição na variável resposta 

resposta = requests.get(API_link, params=parametros)

print(resposta.status_code)
# Status code: 200(sucesso) ou 401(erro)

print(resposta.content)

if resposta.status_code == 200:
    print("Requisição realizada com sucesso")
    dados = resposta.json()   # Armazenando os dados em formato json na variável dados
    #pprint(dados)  #.json()
    temperatura = dados["stadium"]["start"]   # Armazenando a temp em C°
    descricao = dados["sports"]["condition"]["string"]   # Armazenando a descrição
    print(f"A temperatura atual da cidade escolhida é de: {temperatura}")
    print(f"Descrição do clima: {descricao}")
else:
    print("Erro na requisição.")