'''
Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. 
A soma desses múltiplos é 23.
Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.
'''
class MultiplesSumCalculator:
    def __init__(self, limit):
        self.limit = limit  # Inicializa a instância com o limite fornecido

    def calculate_sum(self):
        total_sum = 0  # Inicializa a variável de soma

        for number in range(self.limit):  # Itera por todos os números de 0 até (limite - 1)
            if number % 3 == 0 or number % 5 == 0:  # Verifica se o número é múltiplo de 3 ou 5
                total_sum += number  # Adiciona o número à soma

        return total_sum  # Retorna a soma total

# Exemplo de uso:
limit = 1000  # Define o limite como 1000
calculator = MultiplesSumCalculator(limit)  # Cria uma instância da classe com o limite
result = calculator.calculate_sum()  # Chama o método para calcular a soma
print("A soma de todos os múltiplos de 3 ou 5 abaixo de 1000 é:", result)  # Imprime o resultado
