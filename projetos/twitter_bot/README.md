## Como usar </br></br>


### API atualiza o Twitter de forma automática</br>

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Executar
```bash
python twitter.py
```
- api_key (chave de API): Esta é a chave de API do Twitter, que você obtém registrando um aplicativo no Portal de Desenvolvedores do Twitter. </br>
Após criar o aplicativo, você receberá uma chave de API que será usada para autenticação.

- api_key_secret (segredo da chave de API): Junto com a chave de API, você também receberá um segredo da chave de API ao criar o aplicativo no Portal de Desenvolvedores do Twitter. </br>
Esse segredo da chave de API é uma informação sensível e deve ser mantido em sigilo.

- access_token (token de acesso): Após criar o aplicativo no Portal de Desenvolvedores do Twitter, você precisará gerar um token de acesso. </br>
Esse token é vinculado à sua conta do Twitter e fornece acesso aos recursos da API. No Portal de Desenvolvedores do Twitter, você pode gerar um token de acesso para o aplicativo que criou.

- access_token_secret (segredo do token de acesso): O segredo do token de acesso é fornecido juntamente com o token de acesso ao gerá-lo. </br>
Assim como o segredo da chave de API, o segredo do token de acesso também é uma informação sensível que deve ser mantida em sigilo. </br></br>

Certifique-se de substituir as strings "sua chave de API", "seu segredo de chave", "seu token de acesso" e "seu segredo de token" pelas informações corretas da sua conta do Twitter para garantir a autenticação correta na API do Twitter.