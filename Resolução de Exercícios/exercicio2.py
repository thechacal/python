'''
A função `BracketCombinations(num)` recebe um número inteiro `num` maior ou igual a zero e deve retornar
a quantidade de combinações válidas que podem ser formadas com `num` pares de parênteses. 
Por exemplo, se o valor de entrada for 3, as combinações possíveis com 3 pares de parênteses são: 
()()(), ()(()), (())(), ((())), e (()()). 
Existem 5 combinações no total quando o valor de entrada é 3, então o programa deve retornar 5.
'''
class BracketCombinations:
    def __init__(self):
        self.memoization = {}  # Dicionário para memoização

    def count_combinations(self, num):
        if num < 0:
            return 0  # Se o número de pares de parênteses for negativo, não há combinações válidas
        if num == 0:
            return 1  # Caso base: se não houver pares de parênteses, há uma combinação vazia

        # Verificar se o resultado já foi calculado anteriormente
        if num in self.memoization:
            return self.memoization[num]

        # Inicializar o contador de combinações
        combinations = 0

        # Para cada posição de abertura de parênteses
        for i in range(num):
            # Recursivamente contar as combinações para a parte à esquerda e direita
            left_combinations = self.count_combinations(i)
            right_combinations = self.count_combinations(num - 1 - i)

            # Multiplicar as combinações à esquerda e à direita para obter o total
            combinations += left_combinations * right_combinations

        # Armazenar o resultado na memoização e retornar
        self.memoization[num] = combinations
        return combinations

# Função para contar as combinações válidas de parênteses
def BracketCombinationsCount(num):
    if num < 0:
        return 0  # Se o número de pares de parênteses for negativo, não há combinações válidas
    else:
        counter = BracketCombinations()  # Cria uma instância da classe BracketCombinations
        return counter.count_combinations(num)  # Chama o método count_combinations na instância

# Exemplo de uso:
num = 3
result = BracketCombinationsCount(num)  # Chama a função para contar combinações válidas
print(f"Para {num} pares de parênteses, existem {result} combinações válidas.")  # Imprime o resultado
