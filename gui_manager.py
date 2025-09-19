import tkinter as tk
from calculadora_core import CalculadoraCore

class GerenciadorGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("300x400")
        master.resizable(False, False)

        self.calculadora = CalculadoraCore()
        
        self.display_var = tk.StringVar()
        
        self._criar_widgets()

    def _criar_widgets(self):
        
        display = tk.Entry(self.master, textvariable=self.display_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify="right")
        display.grid(row=0, column=0, columnspan=4, pady=10)

        
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', 'x',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        linha = 1
        coluna = 0

        for texto_botao in botoes:
            comando = self._obter_comando(texto_botao)
            
            botao = tk.Button(self.master, text=texto_botao, font=("Arial", 18), padx=20, pady=20, command=comando)
            botao.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)

    def _obter_comando(self, texto):
        
        if texto == '=':
            return self._comando_calcular
        elif texto == 'C':
            return self._comando_limpar
        else:
            return lambda: self._comando_adicionar(texto)

    def _comando_adicionar(self, char):
        novo_display = self.calculadora.adicionar_caractere(char)
        self.display_var.set(novo_display)

    def _comando_calcular(self):
        novo_display = self.calculadora.calcular_resultado()
        self.display_var.set(novo_display)
        
    def _comando_limpar(self):
        novo_display = self.calculadora.limpar()
        self.display_var.set(novo_display)