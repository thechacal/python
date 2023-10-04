'''
A função `LongestWord(sen)` recebe o parâmetro `sen` e deve retornar a palavra mais longa na string. 
Se houver duas ou mais palavras com o mesmo comprimento, deve-se retornar a primeira palavra da string
com esse comprimento. A função deve ignorar pontuação e assume que `sen` não estará vazio. 
As palavras também podem conter números, por exemplo, "Hello world123 567".
'''
import re  # Importa o módulo de expressões regulares

class LongestWordFinder:
    def __init__(self, sen):
        self.sen = sen  # Inicializa a instância com a string de entrada

    def remove_punctuation(self):
        # Remove a pontuação da string usando expressões regulares
        self.sen = re.sub(r'[^\w\s]', '', self.sen)  # Remove qualquer caractere que não seja palavra (\w) ou espaço em branco (\s)

    def find_longest_word(self):
        # Divide a string em palavras usando espaços em branco como delimitador
        words = self.sen.split()  # Divide a string em uma lista de palavras

        # Inicializa a variável para a palavra mais longa
        longest_word = ""

        for word in words:  # Percorre todas as palavras na lista
            if len(word) > len(longest_word):  # Verifica se a palavra atual é mais longa que a palavra mais longa anterior
                longest_word = word  # Atualiza a palavra mais longa se a condição for verdadeira

        return longest_word  # Retorna a palavra mais longa encontrada

# Exemplo de uso:
sen = "Hello world123, 567! This is a test sentence."  # Define a string de entrada
finder = LongestWordFinder(sen)  # Cria uma instância da classe LongestWordFinder com a string de entrada
finder.remove_punctuation()  # Chama o método para remover a pontuação
result = finder.find_longest_word()  # Chama o método para encontrar a palavra mais longa
print("A palavra mais longa na string é:", result)  # Imprime a palavra mais longa encontrada
