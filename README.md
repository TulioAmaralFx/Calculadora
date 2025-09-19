# Calculadora Tkinter

Este projeto é uma calculadora simples com interface gráfica desenvolvida em Python utilizando a biblioteca Tkinter.

## Funcionalidades

- Operações básicas: soma, subtração, multiplicação e divisão
- Interface gráfica amigável
- Tratamento de erros (divisão por zero e erros de sintaxe)
- Botão para limpar a expressão

## Estrutura dos arquivos

- `main.py`: Arquivo principal para iniciar a aplicação.
- `gui_manager.py`: Gerencia a interface gráfica (GUI) da calculadora.
- `calculadora_core.py`: Contém a lógica central da calculadora.
- `test_calculadora_core.py`: Testes unitários para a lógica da calculadora.

## Como executar

1. Certifique-se de ter o Python 3 instalado com suporte ao Tkinter.
2. No terminal, navegue até a pasta do projeto:
   ```sh
   cd /Users/tuliofernandesamaral/python-vs/teste
   ```
3. Execute o programa:
   ```sh
   python3 main.py
   ```
   ou
   ```sh
   /homebrew/bin/python3.12 main.py
   ```

## Como testar

Execute os testes unitários com:
```sh
python3 test_calculadora_core.py
```

## Requisitos

- Python 3.x
- Tkinter

## Autor

Tulio Fernandes Amaral
