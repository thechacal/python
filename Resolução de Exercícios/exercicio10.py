'''
A função `FirstFactorial(num)` recebe o parâmetro `num` e deve retornar o fatorial dele. 
Por exemplo: se `num` for igual a 4, o programa deve retornar (4 * 3 * 2 * 1) = 24. 
Para os casos de teste, o intervalo de valores de `num` estará entre 1 e 18, e a entrada será
sempre um número inteiro.
'''
class FactorialCalculator:
    def __init__(self):
        pass  # O construtor não realiza nenhuma ação específica, então usamos "pass" para indicar isso

    def calculate_factorial(self, num):
        if num == 0 or num == 1:
            return 1  # Se num for 0 ou 1, o fatorial é 1, então retornamos 1
        else:
            return num * self.calculate_factorial(num - 1)  # Caso contrário, usamos uma abordagem recursiva para calcular o fatorial

# Exemplo de uso:
num = 4  # Define o valor de num
calculator = FactorialCalculator()  # Cria uma instância da classe FactorialCalculator
result = calculator.calculate_factorial(num)  # Chama o método para calcular o fatorial
print(f"O fatorial de {num} é {result}")  # Imprime o resultado
