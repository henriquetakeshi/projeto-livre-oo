class Operacao:
    def __init__(self, valor1, valor2):
        self._valor1 = valor1
        self._valor2 = valor2

    def calcular(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
    
class Soma(Operacao):
    def calcular(self):
        return self._valor1 + self._valor2

class Subtracao(Operacao):
    def calcular(self):
        return self._valor1 - self._valor2

class Multiplicacao(Operacao):
    def calcular(self):
        return self._valor1 * self._valor2

class Divisao(Operacao):
    def calcular(self):
        if self._valor2 == 0:
            return "Erro: Divisão por zero não é permitida."
        return self._valor1 / self._valor2