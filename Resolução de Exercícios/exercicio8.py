'''
A função `FirstReverse(str)` recebe o parâmetro `str` e deve retornar a string em ordem reversa. 
Por exemplo, se a string de entrada for "Hello World and Coders", o programa deve retornar a 
string "sredoC dna dlroW olleH".
'''
class StringReverser:
    def __init__(self, input_str):
        self.input_str = input_str  # Inicializa a instância com a string de entrada fornecida

    def reverse(self):
        # Usamos a função de fatiamento [::-1] para inverter a string
        return self.input_str[::-1]  # Retorna a string de entrada invertida

# Exemplo de uso:
input_str = "Hello World and Coders"  # Define a string de entrada
reverser = StringReverser(input_str)  # Cria uma instância da classe StringReverser
result = reverser.reverse()  # Chama o método para inverter a string
print(result)  # Deve retornar "sredoC dna dlroW olleH" (a string invertida)
