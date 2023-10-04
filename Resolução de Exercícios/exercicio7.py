'''
A função `QuestionsMarks(str)` recebe um parâmetro `str`, que é uma string contendo números de um único
dígito, letras e pontos de interrogação. O objetivo é verificar se existem exatamente 3 pontos
de interrogação entre cada par de dois números que somam 10. Se sim, a função deve retornar a string "true"; 
caso contrário, deve retornar a string "false". Se não houver dois números que somem 10 na string, 
a função também deve retornar "false".

Por exemplo: se `str` for "arrb6???4xxbl5???eee5", a função deve retornar "true" porque há exatamente 3 pontos
de interrogação entre 6 e 4, e 3 pontos de interrogação entre 5 e 5 no final da string.
'''

class QuestionMarksValidator:
    def __init__(self, str):
        self.str = str  # Armazena a string fornecida como atributo da instância
        self.first_num = None  # Inicializa a variável para rastrear o primeiro número
        self.question_count = 0  # Inicializa a variável para rastrear a contagem de pontos de interrogação
        self.result = "false"  # Inicializa o resultado como "false" por padrão

    def validate(self):
        for char in self.str:  # Percorre a string
            if char.isdigit():  # Se o caractere for um dígito
                if self.first_num is None:  # Se for o primeiro número encontrado
                    self.first_num = int(char)  # Armazena o primeiro número
                else:  # Se for o segundo número encontrado
                    second_num = int(char)  # Armazena o segundo número
                    if self.first_num + second_num == 10:  # Verifica se a soma é igual a 10
                        if self.question_count != 3:  # Verifica se não há exatamente 3 pontos de interrogação entre os números
                            return  # Se a condição não for atendida, encerra a validação
                        self.result = "true"  # Define o resultado como "true" se a condição for atendida
                    self.first_num = second_num  # Atualiza o primeiro número para o próximo par
                    self.question_count = 0  # Reseta a contagem de pontos de interrogação para o próximo par
            elif char == "?":  # Se o caractere for um ponto de interrogação
                self.question_count += 1  # Incrementa a contagem de pontos de interrogação

# Exemplo de uso:
str_input = "arrb6???4xxbl5???eee5"
validator = QuestionMarksValidator(str_input)  # Cria uma instância da classe
validator.validate()  # Chama o método para validar a string
result = validator.result  # Obtém o resultado da validação
print(result)  # Deve retornar "true"
