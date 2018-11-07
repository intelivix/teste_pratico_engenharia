# teste_pratico_engenharia (WIP)
Teste prático para os candidatos a desenvolvedor no time de "Engenharia de Dados" da Intelivix.

---

Nos links abaixo estão algumas bases de dados que poderão ser utilizadas durante o exercício:

* **[dataset-0.json](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-0.json)** **([md5](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-0.md5))** -  **71.5 Mb**
* **[dataset-1.json](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-1.json)** **([md5](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-1.md5))** - **147.9 Mb**
* **[dataset-2.json](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-2.json)** **([md5](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-2.md5))** - **364.6 Mb**
* **[dataset-3.json](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-3.json)** **([md5](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-3.md5))** - **716.7 Mb**
* **[dataset-4.json](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-4.json)** **([md5](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-4.md5))** -   **1.5 Gb**
* **[dataset-5.json](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-5.json)** **([md5](https://s3.amazonaws.com/intelivix-datasets/testes_praticos/dataset-5.md5))** -   **2.3 Gb**

As bases só variam em tamanho e seus itens seguem o seguinte formato:

```json
{
    "id": "263c9996-5f74-6412-e01f-cbecdca71c5e",
    "npu": "1517345-36.2016.8.01.0560",
    "estado": "PB",
    "spider": "projudi-rn",
    "juiz": "Saulo Braga Santana Falcão",
    "data_distribuicao": "1990-09-06T14:08:01Z",
    "data_captura": "2017-12-27T17:04:29Z",
    "andamentos": [
        {
            "texto": "denmark quest strip upgrade rocky ... opportunity",
            "data": "1993-12-02T15:40:49Z",
            "etiquetas": [
                "Yellow",
                "Pink",
                "Magenta"
            ]
        },
    ]
}
```

### O desafio consiste nas seguintes etapas:

1. Carregar uma das bases de dados listadas acima em um banco de dados MongoDB.

2. Responder as seguintes consultas:
  1. Contagem total dos items.
  2. Contagem dos andamentos.
  3. Contagem de items por estado.
  4. Contagem de juízes que começam com 'S'.
  5. Contagem de etiquetas mais comuns.

3. Lendo os dados a partir do MongoDB transformá-los e carregar o resultado
em uma tabela do PostgreSQL.
  - Gerar 2 modelos () no SQLAlchemy
  - Realizar as transformações abaixo:
    1. Qual andamento mais antigo com o termo "cinema"
    2. ...
    3. ...
  - Responder as seguintes consultas:
    1. ...
    2. ...
    3. ...

4. Exportar os dados do PostgreSQL para um arquivo chamado `report.csv`.

###  Sobre a entrega:

- As bases possuem alguns erros propositalmente.
- Quanto maior a base, maior a dificuldade.
- Disserte e documente seu código.
- Guarda o tempo de todas as consultas e operações.
- Pense na replicabilidade do teste. Se possível use Docker.
- O escopo de tempo da tarefa é de 1 semana.
- Registrar o tempo despendido para o desenvolvimento.
- O código deve estar público no Github.

###  Ferramentas Sugeridas:
- Python 3
  - Jupyter Notebook
  - PyMongo
  - SQLAlchemy
  - Celery
- Docker (imagem do postgresql, imagem do mongodb, imagem do rabbitmq)

__Quaisquer dúvidas podem ser enviadas para arthur@intelivix.com.__

__Boa sorte!__
