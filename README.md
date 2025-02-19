# Sistema de Finanças Pessoais

Este projeto foi desenvolvido como parte do desafio **4Days4Projects** da Pythonando, ministrado pelo professor Caio. O objetivo é criar um sistema de finanças pessoais usando Python e SQLModel.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **SQLModel**: Biblioteca para interação com banco de dados.
- **SQLite**: Banco de dados para armazenamento local.
- **Matplotlib**: Biblioteca para geração de gráficos.

## Funcionalidades

- **Criação de Contas**: Crie contas bancárias com saldo inicial e banco específico.
- **Listagem de Contas**: Veja todas as contas cadastradas.
- **Desativação de Contas**: Desative contas que não possuem saldo.
- **Transferência de Saldo**: Transfira saldo entre contas.
- **Movimentação de Dinheiro**: Realize entradas e saídas de dinheiro em contas.
- **Total de Contas**: Veja o saldo total de todas as contas.
- **Filtro de Histórico**: Filtre o histórico de movimentações por data.
- **Gráfico de Contas**: Visualize o saldo das contas em um gráfico de barras.

## Padrão MVT (Model-View-Template)

O projeto segue o padrão **MVT**, que é uma variação do padrão **MVC (Model-View-Controller)**. Aqui está como ele é aplicado:

1. **Model (`models.py`)**:

   - Define a estrutura dos dados e as regras de negócio.
   - Contém as classes `Conta` e `Historico`, que representam as tabelas do banco de dados.
   - Usa enums (`Bancos`, `Status`, `Tipos`) para definir valores pré-definidos.

2. **View (`views.py`)**:

   - Contém a lógica de negócio e a interação com o banco de dados.
   - Implementa funções como `criar_conta`, `listar_contas`, `transferir_saldo`, etc.
   - Processa as entradas do usuário e decide o que será exibido.

3. **Template (`templates.py`)**:
   - Responsável pela interface do usuário.
   - Implementa a classe `UI`, que exibe menus e coleta entradas do usuário.
   - Exibe os dados fornecidos pela View.

## Como Executar

1. **Instalação das Dependências**:
   ```bash
   pip install sqlmodel matplotlib
   ```
2. **Execução do Projeto**:

```bash
python templates.py
```

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
