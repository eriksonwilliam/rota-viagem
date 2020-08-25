# Rota de Viagem #

Um turista deseja viajar pelo mundo pagando o menor preço possível independentemente do número de conexões necessárias.
Vamos construir um programa que facilite ao nosso turista, escolher a melhor rota para sua viagem.

Para isso precisamos inserir as rotas através de um arquivo de entrada.

## Input Example ##
```csv
GRU,BRC,10
BRC,SCL,5
GRU,CDG,75
GRU,SCL,20
GRU,ORL,56
ORL,CDG,5
SCL,ORL,20
```

## Explicando ## 
Caso desejemos viajar de **GRU** para **CDG** existem as seguintes rotas:

1. GRU - BRC - SCL - ORL - CDG ao custo de **$40**
2. GRU - ORL - CGD ao custo de **$64**
3. GRU - CDG ao custo de **$75**
4. GRU - SCL - ORL - CDG ao custo de **$48**
5. GRU - BRC - CDG ao custo de **$45**

O melhor preço é da rota **1** logo, o output da consulta deve ser **GRU - BRC - SCL - ORL - CDG**.

### Execução do programa ###
A inicializacao do teste se dará por linha de comando onde o primeiro argumento é o arquivo com a lista de rotas inicial.

para executar o serviço rest
```shell
$ python run.py input-routes.csv
```

para executar o console
```shell
$ python console.py input-routes.csv
```

Duas interfaces de consulta devem ser implementadas:
- Interface de console deverá receber um input com a rota no formato "DE-PARA" e imprimir a melhor rota e seu respectivo valor.
  Exemplo:
  ```shell
  please enter the route: GRU-CGD
  best route: GRU - BRC - SCL - ORL - CDG > $40
  please enter the route: BRC-CDG
  best route: BRC - ORL > $30
  ```

- Interface Rest
    A interface Rest deverá suportar:
    - Registro de novas rotas. Essas novas rotas devem ser persistidas no arquivo csv utilizado como input(input-routes.csv),
    - Consulta de melhor rota entre dois pontos.

Também será necessária a implementação de 2 endpoints Rest, um para registro de rotas e outro para consula de melhor rota.

## Estrutura dos arquivos/pacotes ##
```
rota-viagem
├───Controllers
│   ├───Main.py
│
├───Models
│   ├───File.py
│   ├───SearchRoute.py
│
├───console.py
│
├───run.py
```

## Decisões de design adotadas para a solução ##
Foi utilizado o TDD (Test Driven Development) deviddo seguintes as vantagens oferecidas por essa abordagem:
- Qualidade do código 
- Segurança

Com o objetivo de ser:
- Testável.
- de Facil manutenção.

## Descrição simpples da API Rest ##
POST: localhost:5000/api/create 

body
```shell
{
    "origin": "MAO",
    "destiny" : "REC",
    "amount": 100
}
```
retorno
```shell
{
  "message": "New route successfully created"
}
```

POST: localhost:5000/api/search 

body
```shell
{
    "origin": "GRU",
    "destiny" : "CDG"
}
```
retorno
```shell
{
  "amount": 40,
  "route": "GRU-BRC-SCL-ORL-CDG"
}
```


## Recomendações ##
Para uma melhor fluides da nossa conversa, atente-se aos seguintes pontos:

* Envie apenas o código fonte,
* Estruture sua aplicação seguindo as boas práticas de desenvolvimento,
* Evite o uso de frameworks ou bibliotecas externas à linguagem. Utilize apenas o que for necessário para a exposição do serviço,
* Implemente testes unitários seguindo as boas praticas de mercado,
* Documentação
  Em um arquivo Texto ou Markdown descreva:
  * Como executar a aplicação,
  * Estrutura dos arquivos/pacotes,
  * Explique as decisões de design adotadas para a solução,
  * Descreva sua APÌ Rest de forma simplificada.
