class CalculadoraCore:
    
    def __init__(self):
        self.expressao = ""

    def adicionar_caractere(self, char):
        self.expressao += str(char)
        return self.expressao

    def calcular_resultado(self):
        
        try:
            expressao_para_eval = self.expressao.replace("x", "*")
            
            resultado = str(float(eval(expressao_para_eval)))
            self.expressao = resultado
            return resultado
        except ZeroDivisionError:
            self.expressao = ""
            return "Erro: Divisão por 0"
        except:
            self.expressao = ""
            return "Erro de Sintaxe"

    def limpar(self):
        self.expressao = ""
        return ""