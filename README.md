# GaleriaSM
> Página para exposição de fotos enviadas por usuários com aprovação simples por usuário moderador


Você tem um casal de amigos que irá se casar em breve e eles pediram para fazer uma brincadeira com os convidados. Eles querem criar uma galeria de fotos onde todo mundo poderá subir fotos tiradas durante o casamento.
Você irá precisar desenvolver 3 telas:
 1. Uma tela de upload de fotos
 2. Uma tela para exibir a galeria
 3. Uma tela para realizar aprovação das fotos para visualizar na galeria.

Apenas fotos que foram aprovadas devem ser visíveis na página da galeria que será visível para todos.
As fotos são armazenadas na AWS S3.
O projeto é desenvolvido em python utilizando Flask.


## Setup de desenvolvimento

```sh
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install python-dotenv
pip install boto3
flask run
```

## Histórico

* 0.3.1
    * Fluxo de telas estabelecido
* 0.3.0
    * Reorganização de arquivos
* 0.2.1
    * Conexão com AWS S3, upload e carregamento de imagens
* 0.2.0
    * Correção no .gitignore
* 0.1.1
    * Lista de nomes substituída por lista de imagens
* 0.1.0
    * Correção de diretórios
    * Correção do .gitignore
* 0.0.1
    * Primeira tela, com lista de nomes
  

## Contato

[Jordy Araújo](jordyaraujo.github.io) – [@TimbuAstronauta](https://twitter.com/TimbuAstronauta) – jordyaraujo@outlook.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/jordyaraujo](https://github.com/jordyaraujo/)

## Contributing

1. Fork it (<https://github.com/JordyAraujo/DesafioSurfMappers/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request