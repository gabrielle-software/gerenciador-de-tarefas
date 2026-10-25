# Gerenciador de Tarefas em Python

Projeto desenvolvido em Python com o objetivo de praticar lógica de programação, manipulação de arquivos e persistência de dados.

O Gerenciador de Tarefas permite cadastrar, listar, concluir e excluir tarefas por meio de um menu interativo no terminal. Os dados são armazenados em um arquivo JSON, permitindo que as tarefas permaneçam salvas entre execuções do programa.

## Funcionalidades

- **Adicionar tarefas:** cadastra novas tarefas com descrição.
- **Listar tarefas:** exibe as tarefas cadastradas e seus status.
- **Concluir tarefas:** atualiza o status de uma tarefa para concluída.
- **Excluir tarefas:** remove uma tarefa da lista.
- **Persistência de dados:** salva e carrega as tarefas utilizando um arquivo JSON.
- **Validação de entradas:** trata descrições vazias, números inválidos e opções incorretas do menu.

## Tecnologias utilizadas

- Python 3
- JSON
- Biblioteca padrão `pathlib`

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

Esse arquivo contém as descrições das tarefas e seus respectivos status.

## Estrutura do projeto

```text
gerenciador-de-tarefas/
├── main.py
├── README.md
└── tarefas.json  # Criado durante a execução
```

**Observação:** o arquivo `tarefas.json` é gerado durante o uso do programa e pode não estar presente no repositório inicialmente.

## Objetivo acadêmico e profissional

Este projeto faz parte da prática de desenvolvimento de software, com foco em lógica de programação, organização de código, manipulação de dados e utilização do GitHub para versionamento e apresentação de projetos.

## Autora

Desenvolvido como projeto de prática em Python.

**Repositório:** https://github.com/gabrielle-software/gerenciador-de-tarefas


## Exemplo de utilização

Ao executar o programa, o usuário pode interagir com um menu no terminal para gerenciar suas tarefas.

Exemplo das operações disponíveis:

* Adicionar uma nova tarefa.
* Visualizar as tarefas cadastradas.
* Marcar uma tarefa como concluída.
* Excluir uma tarefa.
* Encerrar o programa.

## Aprendizados

Com o desenvolvimento deste projeto, pratiquei:

* Lógica de programação com Python.
* Criação de funções e menus interativos.
* Leitura e escrita de arquivos JSON.
* Manipulação de caminhos e arquivos com `pathlib`.
* Validação de entradas do usuário.
* Organização de projetos e documentação com GitHub.

