# teste_pratico_engenharia (WIP)
Teste prático para os candidatos a desenvolvedor no time de "Engenharia de Dados" da Intelivix.

---

Nos balde abaixo estão dispostas algumas bases de dados que deverão ser utilizadas:

__s3://intelivix-teste-pratico/engenharia/__

- base-1.json - 30 Mb
- base-2.json - 60 Mb
- base-3.json - 100 Mb
- base-4.json - 300 Mb
- base-5.json - 500 Mb

As bases seguem o seguinte formato:

```json
{
    "id": "",
    "numero": "",
    "estado": "",
    "data": "",
    "andamentos": [
        {
            "texto": "",
            "data": "",
            "etiquetas": [],
        }
    ],
    "spider": "",
    "data-captura": ""
}
```

### O desafio consiste em:

- Carregar uma das bases de dados listadas acima em um banco de dados MongoDB.
- Responder as seguintes consultas:
  1. ...
  2. ...
  3. ...
- Lendo os dados a partir do MongoDB transformá-los e carregar o resultado
em uma tabela do PostgreSQL.
  - Gerar modelo no SQLAlchemy
  - Realizar as transformações abaixo:
    1. ...
    2. ...
    3. ...
  - Responder as seguintes consultas:
    1. ...
    2. ...
    3. ...
- Exportar os dados do PostgreSQL para um arquivo chamado `report.csv`.

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
