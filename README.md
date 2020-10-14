# GaleriaSM
> Aplicação para exposição de fotos enviadas por usuários com aprovação simples por moderador


## Problema proposto

Você tem um casal de amigos que irá se casar em breve e eles pediram para fazer uma brincadeira com os convidados. Eles querem criar uma galeria de fotos onde todo mundo poderá subir fotos tiradas durante o casamento.
Você irá precisar desenvolver 3 telas:
 1. uma tela de upload de fotos
 2. uma tela para exibir a galeria
 3. uma tela para realizar aprovação das fotos para visualizar na galeria.

Apenas fotos que foram aprovadas devem ser visível na página da galeria que será visível para todos.
As fotos precisam ser armazenadas na AWS S3.
O projeto precisa ser desenvolvido em python utilizando qualquer framework de sua escolha.

Estarei observando qualidade e organização do código, arquitetura da solução, ocorrência de bugs, qualidade da interface, responsividade e a robustez da solução em geral. 

Para submeter o teste você deve disponibilizar o código em algum repositório público e hospedar o projeto em algum servidor para que eu possa testar.


## Solução

O projeto foi dividido em três telas, como solicitado.
A tela inicial mostra a galeria com as imagens enviadas pelos usuários e aprovadas pelo moderador.
A tela de Upload tem um formulário simples para envio de imagens pelos usuários comuns.
A tela de aprovação é visível apenas para usuários logados e permite visualizar todas as imagens salvas e selecionar quais deverão ser mostradas na galeria.


## Setup de desenvolvimento

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
flask run
```  
> Definir as credenciais AWS em /config.py


## Autor

Jordy Araújo – jordyaraujo@outlook.com