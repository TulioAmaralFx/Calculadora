import unittest
from calculadora_core import CalculadoraCore

class CalculadoraTestes(unittest.TestCase):
    
    def setUp(self):
        self.calc = CalculadoraCore()

    def test_adicionar_caractere(self):
        self.calc.adicionar_caractere('1')
        self.calc.adicionar_caractere('+')
        self.calc.adicionar_caractere('2')
        self.assertEqual(self.calc.expressao, '1+2')

    def test_calcular_resultado_soma(self):
        self.calc.adicionar_caractere('1')
        self.calc.adicionar_caractere('+')
        self.calc.adicionar_caractere('2')
        resultado = self.calc.calcular_resultado()
        self.assertEqual(resultado, '3.0')

    def test_calcular_resultado_multiplicacao(self):
        self.calc.adicionar_caractere('3')
        self.calc.adicionar_caractere('x')
        self.calc.adicionar_caractere('4')
        resultado = self.calc.calcular_resultado()
        self.assertEqual(resultado, '12.0')

    def test_divisao_por_zero(self):
        self.calc.adicionar_caractere('5')
        self.calc.adicionar_caractere('/')
        self.calc.adicionar_caractere('0')
        resultado = self.calc.calcular_resultado()
        self.assertEqual(resultado, 'Erro: Divisão por 0')

    def test_erro_sintaxe(self):
        self.calc.adicionar_caractere('1')
        self.calc.adicionar_caractere('+')
        resultado = self.calc.calcular_resultado()
        self.assertEqual(resultado, 'Erro de Sintaxe')

    def test_limpar(self):
        self.calc.adicionar_caractere('9')
        self.calc.limpar()
        self.assertEqual(self.calc.expressao, '')

if __name__ == '__main__':
    unittest.main()