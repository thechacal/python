'''
A função `BracketMatcher(str)` recebe a string `str` como parâmetro e deve retornar 1 se os parênteses
estiverem corretamente combinados e cada um estiver devidamente fechado. Caso contrário, deve retornar 0. 
Por exemplo: se `str` for "(hello (world))", o resultado deve ser 1, 
mas se `str` for "((hello (world))", o resultado deve ser 0 porque os parênteses não estão corretamente 
combinados. Apenas os caracteres "(" e ")" serão usados como parênteses. 
Se `str` não contiver parênteses, a função deve retornar 1.
'''
class BracketMatcher:
    def __init__(self, input_str):
        self.input_str = input_str  # Inicializa a string de entrada
        self.stack = []  # Inicializa uma lista (pilha) para rastrear os parênteses abertos

    def match(self):
        for char in self.input_str:  # Itera por cada caractere na string de entrada
            if char == "(":  # Se encontrarmos um parêntese aberto
                self.stack.append(char)  # Adiciona o parêntese aberto à pilha
            elif char == ")":  # Se encontrarmos um parêntese fechado
                if not self.stack:  # Verifica se a pilha está vazia (sem parênteses abertos correspondentes)
                    return 0  # Retorna 0, pois os parênteses não estão corretamente combinados
                self.stack.pop()  # Remove o parêntese aberto correspondente da pilha

        # Após percorrer toda a string, verificamos se a pilha está vazia
        # Se a pilha estiver vazia, todos os parênteses foram corretamente combinados
        # Caso contrário, os parênteses não estão corretamente combinados
        return 1 if not self.stack else 0

# Exemplos de uso:
matcher1 = BracketMatcher("(hello (world))")
print(matcher1.match())  # Deve retornar 1, pois os parênteses estão corretamente combinados

matcher2 = BracketMatcher("((hello (world))")
print(matcher2.match())  # Deve retornar 0, pois os parênteses não estão corretamente combinados

matcher3 = BracketMatcher("No parentheses here")
print(matcher3.match())  # Deve retornar 1, pois não há parênteses na string
