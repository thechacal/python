'''
A função `MinWindowSubstring(strArr)` recebe um array de strings `strArr`, que conterá apenas duas strings. 
O primeiro parâmetro será a string N e o segundo parâmetro será uma string K com alguns caracteres. 
O objetivo é determinar a menor substring de N que contenha todos os caracteres em K.

Por exemplo: se `strArr` for ["aaabaaddae", "aed"], 
a menor substring de N que contém os caracteres "a", "e" e "d" é "dae", localizada no final da string. 
Portanto, para este exemplo, o programa deve retornar a string "dae".

Outro exemplo: se `strArr` for ["aabdccdbcacd", "aad"], a menor substring de N que contém todos os caracteres
em K é "aabd", localizada no início da string. 
Ambas as strings terão um comprimento entre 1 e 50 caracteres, e todos os caracteres de K existirão 
em algum lugar da string N. Ambas as strings conterão apenas caracteres alfabéticos minúsculos.
'''
class MinWindowSubstring:
    def __init__(self, strArr):
        self.N = strArr[0]  # A primeira string N do strArr
        self.K = strArr[1]  # A segunda string K do strArr
        self.char_count = {}  # Um dicionário para rastrear a contagem de caracteres em K
        self.left = 0  # Variável para rastrear o índice esquerdo da janela
        self.min_len = float('inf')  # Inicializa o comprimento mínimo da substring com infinito
        self.min_window = ""  # Inicializa a substring mínima vazia
        self.count = len(self.K)  # Inicializa o contador de caracteres em K com o tamanho de K
    
    def find_min_window(self):
        for right in range(len(self.N)):  # Percorre a string N
            if self.N[right] in self.char_count:
                self.char_count[self.N[right]] -= 1  # Decrementa a contagem do caractere em K
                if self.char_count[self.N[right]] >= 0:  # Se ainda houver caracteres necessários
                    self.count -= 1  # Decrementa o contador
            
            while self.count == 0:  # Quando todos os caracteres em K são encontrados
                if right - self.left + 1 < self.min_len:  # Verifica se é uma nova substring mínima
                    self.min_len = right - self.left + 1  # Atualiza o comprimento mínimo
                    self.min_window = self.N[self.left:right + 1]  # Atualiza a substring mínima
                
                if self.N[self.left] in self.char_count:
                    self.char_count[self.N[self.left]] += 1  # Restaura a contagem do caractere em K
                    if self.char_count[self.N[self.left]] > 0:  # Se ainda houver caracteres necessários
                        self.count += 1  # Incrementa o contador
                
                self.left += 1  # Move o índice esquerdo para a direita
        
        return self.min_window  # Retorna a menor substring encontrada

# Exemplo de uso:
strArr = ["aaabaaddae", "aed"]
min_window_finder = MinWindowSubstring(strArr)  # Cria uma instância da classe
resultado = min_window_finder.find_min_window()  # Chama o método para encontrar a menor substring
print(resultado)  # Deve imprimir "dae"
