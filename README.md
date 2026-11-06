
# Gerenciador de Tarefas em Python

[![Testes automatizados](https://github.com/gabrielle-software/gerenciador-de-tarefas/actions/workflows/tests.yml/badge.svg)](https://github.com/gabrielle-software/gerenciador-de-tarefas/actions/workflows/tests.yml)

Projeto desenvolvido em Python com o objetivo de praticar lógica de programação, manipulação de arquivos e persistência de dados.

O Gerenciador de Tarefas permite cadastrar, listar, concluir e excluir tarefas por meio de um menu interativo no terminal. Os dados são armazenados em um arquivo JSON, permitindo que as tarefas permaneçam salvas entre execuções do programa.

## Funcionalidades

- **Adicionar tarefas:** cadastra novas tarefas com descrição.
- **Listar tarefas:** exibe as tarefas cadastradas e seus status.
- **Concluir tarefas:** atualiza o status de uma tarefa para concluída.
- **Excluir tarefas:** remove uma tarefa da lista.
- **Persistência de dados:** salva e carrega tarefas utilizando um arquivo JSON.
- **Validação de entradas:** trata descrições vazias, números inválidos e opções incorretas do menu.

## Tecnologias utilizadas

- Python 3
- JSON
- Biblioteca padrão `pathlib`
- Biblioteca `unittest` para testes automatizados

## Como executar o projeto

### Pré-requisitos

- Python 3 instalado no computador.

### Passo a passo

1. Clone o repositório:

```bash
git clone https://github.com/gabrielle-software/gerenciador-de-tarefas.git
```

2. Entre na pasta do projeto:

```bash
cd gerenciador-de-tarefas
```

3. Execute o programa:

```bash
python main.py
```

No Windows, se necessário, utilize `py main.py`. Em alguns sistemas Linux, pode ser necessário utilizar `python3 main.py`.

## Armazenamento de dados

As tarefas são armazenadas no arquivo `tarefas.json`, criado na mesma pasta do arquivo `main.py` quando o programa salva uma tarefa pela primeira vez.

## Testes automatizados

O projeto utiliza a biblioteca `unittest` do Python para verificar funcionalidades como:

- Carregamento de tarefas sem arquivo existente.
- Salvamento e carregamento de tarefas.
- Tratamento de arquivos JSON inválidos.

Para executar os testes localmente:

```bash
python -m unittest -v
```

Os testes também são executados automaticamente pelo GitHub Actions a cada atualização na branch principal.

## Objetivo do projeto

Este projeto faz parte do meu aprendizado em Engenharia de Software, com foco no desenvolvimento de habilidades em Python, lógica de programação, organização de código, persistência de dados e testes automatizados.

---

Desenvolvido por **Gabrielle Sousa**.


