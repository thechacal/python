'''
Jack tem três pratos à sua frente. O gigante tem N feijões que ele distribui entre os três pratos. 
Todos os feijões parecem iguais, mas um deles é um feijão mágico. Jack não sabe qual é o feijão mágico, 
mas o gigante sabe.

Jack pode fazer perguntas ao gigante na forma: "Este subconjunto de feijões contém o feijão mágico?" 
Em cada pergunta, Jack pode escolher qualquer subconjunto de feijões de um único prato, e o gigante 
responderá honestamente.

Se os três pratos contiverem a, b e c feijões, respectivamente, definimos h(a, b, c) como o número mínimo 
de perguntas que Jack precisa fazer para garantir que ele encontre o feijão mágico. 
Por exemplo, h(1, 2, 3) = 3 e h(2, 3, 3) = 4.

Seja H(N) a soma de h(a, b, c) para todas as triplas de números não negativos a, b, c, 
onde 1 ≤ a + b + c ≤ N.

Você tem: H(6) = 203 e H(20) = 7718.

Um repunit, R_n, é um número formado por n dígitos, todos '1'. 
Por exemplo, R_3 = 111 e H(R_3) = 1634144.

Encontre H(R_19). Dê sua resposta módulo 1,000,000,007.
'''
MOD = 1000000007  # Define o valor MOD para cálculos modulo

class BeanMagicGame:
    def __init__(self, n):
        self.n = n  # Inicializa o número de feijões (n)

    def calculate_H(self, a, b, c):
        if a == 0 and b == 0 and c == 0:
            return 0  # Caso base: 0 perguntas necessárias
        if a == 0 or b == 0 or c == 0:
            return a + b + c  # Caso base: soma dos feijões restantes
        # Calcula H(a, b, c) recursivamente
        return min(self.calculate_H(a - 1, b, c), self.calculate_H(a, b - 1, c), self.calculate_H(a, b, c - 1)) + 1

    def calculate_H_Rn(self):
        total = 0
        # Itera sobre todas as triplas possíveis de a, b e c
        for a in range(1, self.n + 1):
            for b in range(1, self.n - a + 2):
                c = self.n - a - b
                total += self.calculate_H(a, b, c)  # Soma os valores de H(a, b, c)
        return total % MOD  # Retorna o resultado final módulo MOD

# Criar uma instância da classe BeanMagicGame com n = 19
n = 19
game = BeanMagicGame(n)

# Encontre H(R_19) e forneça a resposta módulo 1,000,000,007
result = game.calculate_H_Rn()
print("H(R_19) modulo 1,000,000,007 é:", result)  # Imprime o resultado final
