'''
Em um torneio, há n times, e cada time joga duas vezes contra todos os outros times. 

Um time ganha dois pontos por vitória, um ponto por empate e nenhum ponto por derrota.

Com dois times, há três resultados possíveis para o total de pontos: (4,0) quando um time vence duas vezes, 
(3,1) quando um time vence e empata, e (2,2) quando há dois empates ou um time vence um jogo e perde o outro.

Neste caso, não distinguimos os times, então (3,1) e (1,3) são considerados idênticos.

Defina F(n) como o número total de resultados finais possíveis com n times, de forma que F(2) = 3.
Você também tem F(7) = 32923.

Encontre F(100) e forneça sua resposta modulo 10^9+7.
'''
class TournamentResults:
    def __init__(self, n):
        self.n = n  # Inicializa o número de times (n)
        self.MOD = 10**9 + 7  # Define o valor MOD para cálculos modulo

    def calculate_F(self):
        # Inicializa uma matriz para armazenar os resultados intermediários
        dp = [[0] * (self.n + 1) for _ in range(self.n + 1)]

        # Inicializa o caso base para 2 times
        dp[2][0] = 1
        dp[2][1] = 1
        dp[2][2] = 1

        # Preenche a matriz usando programação dinâmica
        for i in range(3, self.n + 1):
            for j in range(self.n + 1):
                dp[i][j] = (dp[i - 1][j] * (j + 1) + dp[i - 2][j] * (i - j - 1)) % self.MOD

        # Calcula o resultado final somando os valores da última linha da matriz
        result = sum(dp[self.n]) % self.MOD

        return result

# Criar uma instância da classe TournamentResults com n = 100
n = 100
tournament = TournamentResults(n)

# Encontre F(100) e forneça a resposta modulo 10^9+7
result = tournament.calculate_F()
print("F(100) modulo 10^9+7 é:", result)