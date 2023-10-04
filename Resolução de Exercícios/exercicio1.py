'''
Exercício 1

Uma empresa comercial possui um programa para controle das receitas e despesas em seus 10 projetos. 
Os projetos são numerados de 0 até 9. 
Faça um programa C que controle a entrada e saída de recursos dos projetos. 
O programa deverá ler um conjunto de informações contendo: 
Número do projeto, valor, tipo despesa ("R" - Receita e "D" - Despesa). 
O programa termina quando o valor do código do projeto for igual a -1. 
Sabe-se que Receita deve ser somada ao saldo do projeto e despesa subtraída do saldo do projeto. 
Ao final do programa, imprirmir o saldo final de cada projeto.

Dica: Usar uma estrutura do tipo vetor para controlar os saldos dos projetos. 
Usar o conceito de struct para agrupar as informações lidas.
'''
# Define a classe Projeto
class Projeto:
    def __init__(self, numero):
        self.numero = numero  # Inicializa o número do projeto
        self.saldo = 0  # Inicializa o saldo do projeto como zero

    def registrar_movimentacao(self, valor, tipo):
        if tipo == "R":
            self.saldo += valor  # Se o tipo for "R", adiciona o valor ao saldo
        elif tipo == "D":
            self.saldo -= valor  # Se o tipo for "D", subtrai o valor do saldo
        else:
            print("Tipo inválido. Use 'R' para Receita ou 'D' para Despesa.")  # Mensagem de erro para tipos inválidos

# Cria uma lista de 10 projetos, numerados de 0 a 9, usando list comprehension
projetos = [Projeto(i) for i in range(10)]

# Entra em um loop que permite registrar movimentações para os projetos
while True:
    numero_projeto = int(input("Digite o número do projeto (-1 para sair): "))
    
    # Verifica se deve sair do loop
    if numero_projeto == -1:
        break
    
    valor = float(input("Digite o valor: "))  # Lê o valor da movimentação
    tipo = input("Digite o tipo (R para Receita, D para Despesa): ").upper()  # Lê o tipo da movimentação e converte para maiúsculas
    
    # Valida o número do projeto
    if 0 <= numero_projeto < 10:
        projetos[numero_projeto].registrar_movimentacao(valor, tipo)  # Registra a movimentação no projeto correspondente
    else:
        print("Número de projeto inválido. Digite um número entre 0 e 9.")  # Mensagem de erro para números de projeto inválidos

# Imprime os saldos finais de cada projeto
for projeto in projetos:
    print(f"Projeto {projeto.numero}: Saldo final = {projeto.saldo}")  # Imprime o saldo final de cada projeto
