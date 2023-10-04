'''
A função `CodelandUsernameValidation(str)` recebe o parâmetro `str` e deve determinar se a string
é um nome de usuário válido de acordo com as seguintes regras:

1. O nome de usuário deve ter entre 4 e 25 caracteres.
2. Deve começar com uma letra.
3. Pode conter apenas letras, números e o caractere de sublinhado (underscore).
4. Não pode terminar com um caractere de sublinhado.

Se o nome de usuário for válido, o programa deve retornar a string "true", caso contrário, 
deve retornar a string "false".
'''
class UsernameValidator:
    def __init__(self, username):
        self.username = username  # Inicializa a instância com o nome de usuário fornecido

    def is_valid(self):
        # Verificar o comprimento da string
        if len(self.username) < 4 or len(self.username) > 25:
            return False  # Retorna False se o comprimento estiver fora do intervalo [4, 25]

        # Verificar se começa com uma letra
        if not self.username[0].isalpha():
            return False  # Retorna False se o primeiro caractere não for uma letra

        # Verificar se contém apenas letras, números e sublinhados
        for char in self.username:
            if not (char.isalnum() or char == "_"):
                return False  # Retorna False se algum caractere não for letra, número ou sublinhado

        # Verificar se não termina com sublinhado
        if self.username[-1] == "_":
            return False  # Retorna False se o nome de usuário terminar com um sublinhado

        # Se todas as verificações passaram, o nome de usuário é válido
        return True  # Retorna True se o nome de usuário passar em todas as verificações

# Exemplos de uso:
validator1 = UsernameValidator("CodeLand123")
print(validator1.is_valid())  # Deve retornar True

validator2 = UsernameValidator("123Invalid")
print(validator2.is_valid())  # Deve retornar False