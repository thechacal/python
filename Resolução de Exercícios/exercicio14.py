'''
Vamos definir D(n) como o enésimo inteiro positivo cuja soma dos dígitos é um número primo.
Por exemplo, D(61) = 157 e D(10^8) = 403539364.

Encontre D(10^16).
'''
class NumberFinder:
    def __init__(self, limit):
        self.limit = limit  # Inicializa o limite (10^16) para D(n)

    @staticmethod
    def is_prime(n):
        # Verifica se um número é primo
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def digit_sum(n):
        # Calcula a soma dos dígitos de um número
        return sum(map(int, str(n)))

    def find_d(self):
        n = 0  # Inicializa o contador de números
        d = 0  # Inicializa o contador de números que atendem ao critério
        while True:
            n += 1  # Gera o próximo número positivo
            if self.is_prime(self.digit_sum(n)):
                d += 1  # Se a soma dos dígitos for primo, incrementa o contador
            if d == self.limit:  # Quando atingir o limite, retorna o número encontrado
                return n

# Criar uma instância da classe NumberFinder com limit = 10^16
limit = 10**16
finder = NumberFinder(limit)

# Encontre D(10^16)
result = finder.find_d()
print("D(10^16) é:", result)  # Imprime o resultado final
