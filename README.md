# K-Buster-API

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:

```shell
pip install pytest-testdox pytest-django
```

5. Agora é só rodar os testes no diretório principal do projeto:

```shell
pytest --testdox -vvs
```

## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

- Rodando testes da Tarefa 1:

```python
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

- Rodando testes da Tarefa 2:

```python
pytest --testdox -vvs tests/tarefas/tarefa_2/
```

- Rodando testes da Tarefa 3:

```python
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

- Rodando testes da Tarefa 4:

```python
pytest --testdox -vvs tests/tarefas/tarefa_4/
```
