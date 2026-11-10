# Auditor de Dados

## Sobre o projeto

O Auditor de Dados é um projeto desenvolvido em Python com o objetivo de identificar informações inválidas em cadastros.

O projeto simula uma etapa de validação e controle de qualidade de dados, ajudando a evitar que informações incorretas sejam utilizadas em sistemas e análises.

## Funcionalidades

- Validar se o nome foi preenchido.
- Verificar se a idade contém apenas números.
- Conferir se a idade está entre 0 e 120 anos.
- Permitir o cadastro de várias pessoas em uma execução.
- Armazenar temporariamente os cadastros válidos.
- Identificar e informar dados inválidos.
- Gerar um relatório com os cadastros válidos e a quantidade de registros.

**Observação:** os cadastros são armazenados apenas na memória durante a execução do programa.

## Tecnologias utilizadas

- Python 3
- Git

## Como executar

1. Instale o Python 3.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

   `python3 main.py`

## Próximas melhorias

- Permitir a validação de vários cadastros.
- Identificar registros duplicados.
- Ler cadastros de arquivos CSV.
- Gerar relatórios de inconsistências.

## Status

Em desenvolvimento — versão inicial de validação individual de cadastros.