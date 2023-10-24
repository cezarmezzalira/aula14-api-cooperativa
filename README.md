# Projeto Aula 14 - Gerenciamento de pátio de cooperativa

Nesta aula, iremos ver mais um exemplo de API REST, desta vez com um CRUD em memória.

Nosso exemplo é o seguinte: Temos uma cooperativa que possui a necessidade de controlar os caminhões que estão dentro do pátio durante a entrega de grãos. O processo atual é através de planilhas que são preenchidas manualmente em planilha de papel e depois são inseridas no sistema através de uma rotina especifica, o que acaba gerando problemas de entendimento e muitas vezes as informações são cadastradas de forma errada.
Para resolver esses problemas, será necessária uma API REST que faça o seguinte: CRUD  (Create, Retrieve, Update e Delete) da entrega de grãos. Ao ser criado o registro, deve conter o nome do motorista, placa do caminhão, peso do caminhão carregado e data e hora de entrada no pátio. Deve listar todos os caminhões que ainda estão no pátio. Deve atualizar o registro com o peso do caminhão vazio e baseado no peso, gravar em um campo o peso da carga, que é a diferença do peso do caminhão carregado pelo peso do caminhão vazio, bem como atualizar a data e hora de saída do pátio. Deve permitir excluir um registro onde o caminhão ainda não saiu do pátio.


## Criar um novo registro

Regra de negócio: Não deixar cadastrar mais de um registro por placa de veículo

POST /registros
body:

```json
{
    "nome_motorista": "Fulano de tal",
    "placa_veiculo": "ABC1A12",
    "peso_bruto": 10000,
}
```

## Listar todos os caminhões no pátio

GET /registros
body: vazio

## Atualizar o registro com o peso final

PATCH /registros/:placa/finalizar

Atualiza apenas com os dados do body passado, ou seja, uma atualização parcial

body:

```json
{
    "peso_final": 3500
}
```

DELETE /registros/:placa

Só pode excluir um registro se o caminhão ainda estiver no pátio

body: vazio

