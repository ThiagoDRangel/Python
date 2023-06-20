import tweepy
import requests
import json

# Informações de autenticação
api_key = "sua chave de API"
api_key_secret = "seu segredo de chave"
access_token = "seu token de acesso"
access_token_secret = "seu segredo de token"

# Configuração da autenticação
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

# Criação da instância da API
api = tweepy.API(authenticator, wait_on_rate_limit=True)

# Obtém a citação aleatória
response = requests.get('https://zenquotes.io/api/quotes/')
data = json.loads(response.text)
quote = data[0].get('q')
author = data[0].get('a')
description = f"{quote}\n - {author}"

# Exibe a citação
print(description)
print("Bio Atualizada")

# Atualiza o status do perfil
api.update_profile(description=description)
