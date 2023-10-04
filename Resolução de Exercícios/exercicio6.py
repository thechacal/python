'''
A função `FindIntersection(strArr)` recebe um array de strings chamado `strArr`, que conterá 2 elementos: 
o primeiro elemento representa uma lista de números separados por vírgula, ordenados em ordem crescente; 
o segundo elemento representa outra lista de números separados por vírgula, também ordenados. 
O objetivo é retornar uma string contendo os números que ocorrem em ambos os elementos de `strArr`, 
em ordem crescente e separados por vírgula. Se não houver interseção, a função deve retornar a string "false".
'''
class IntersectionFinder:
    def __init__(self, strArr):
        # Divide as strings em listas de números inteiros
        self.list1 = [int(num) for num in strArr[0].split(",")]
        self.list2 = [int(num) for num in strArr[1].split(",")]
        self.intersection = []  # Inicializa uma lista para armazenar os números de interseção

    def find_intersection(self):
        i, j = 0, 0  # Inicia dois índices para percorrer as duas listas

        # Encontra a interseção das duas listas
        while i < len(self.list1) and j < len(self.list2):
            if self.list1[i] == self.list2[j]:
                self.intersection.append(str(self.list1[i]))  # Adiciona o número à lista de interseção
                i += 1
                j += 1
            elif self.list1[i] < self.list2[j]:
                i += 1
            else:
                j += 1

        # Verifica se há interseção
        if len(self.intersection) > 0:
            return ",".join(self.intersection)  # Converte a lista de interseção em uma string separada por vírgulas
        else:
            return "false"  # Retorna "false" se não houver interseção

# Exemplo de uso:
strArr = ["1,3,4,7,10", "2,3,5,7,8"]
intersection_finder = IntersectionFinder(strArr)  # Cria uma instância da classe
result = intersection_finder.find_intersection()  # Chama o método para encontrar a interseção
print(result)  # Deve retornar "3,7"
