'''
Este problema envolve um procedimento iterativo que começa com um círculo de n ≥ 3 inteiros. 
Em cada etapa, cada número é substituído simultaneamente pela diferença absoluta de seus dois vizinhos.

Para qualquer valor inicial, o procedimento eventualmente se torna periódico.

Defina S(N) como a soma de todos os possíveis períodos para 3 ≤ n ≤ N. 
Por exemplo, S(6) = 6, porque os períodos possíveis para 3 ≤ n ≤ 6 são 1, 2, 3. 
Especificamente, n=3 e n=4 podem ter apenas o período 1, enquanto n=5 pode ter o período 1 ou 3, 
e n=6 pode ter o período 1 ou 2.

Você também tem S(30) = 20381.

Encontre S(100).
'''
class PeriodCalculator:
    def __init__(self, N):
        self.N = N  # Inicializa o valor máximo de n para o qual desejamos calcular os períodos
        self.periods = [0] * (N + 1)  # Inicializa uma lista para armazenar os períodos

    def calculate_periods(self):
        # Inicializar com períodos conhecidos para n=3 e n=4
        self.periods[3] = 1
        self.periods[4] = 1

        for n in range(5, self.N + 1):
            # Para cada valor de n, calcular o período com base nos valores anteriores
            # A fórmula para o período é periods[n] = periods[n-1] + periods[n-2]
            self.periods[n] = self.periods[n - 1] + self.periods[n - 2]

    def find_S(self):
        # Somar os períodos para obter S(N)
        S_N = sum(self.periods[3:self.N + 1])
        return S_N

# Criar uma instância da classe PeriodCalculator com N = 100
N = 100
calculator = PeriodCalculator(N)

# Encontre S(100)
result = calculator.find_S()
print("S(100) é:", result)  # Imprime o resultado final
