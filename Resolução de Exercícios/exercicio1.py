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
class Projeto:
    def __init__(self, num):
        self.numero = num
        self.saldo = 0

    def atualizar_saldo(self, valor, tipo_despesa):
        if tipo_despesa.upper() == 'R':
            self.saldo += valor
        elif tipo_despesa.upper() == 'D':
            self.saldo -= valor
        else:
            print("Tipo de despesa inválido! Use 'R' para Receita ou 'D' para Despesa.")

class ControleProjetos:
    def __init__(self):
        self.projetos = []

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)

    def executar(self):
        while True:
            numero_projeto = int(input("Digite o número do projeto (-1 para encerrar): "))

            if numero_projeto == -1:
                break

            valor = float(input("Digite o valor: "))
            tipo_despesa = input("Digite o tipo de despesa (R - Receita, D - Despesa): ").upper()

            projeto_encontrado = False
            for projeto in self.projetos:
                if projeto.numero == numero_projeto:
                    projeto.atualizar_saldo(valor, tipo_despesa)
                    projeto_encontrado = True
                    break

            if not projeto_encontrado:
                print("Projeto não encontrado!")

    def imprimir_saldos(self):
        print("\nSaldo final de cada projeto:")
        for projeto in self.projetos:
            print(f"Projeto {projeto.numero}: R$ {projeto.saldo}")

controle_projetos = ControleProjetos()

NUM_PROJETOS = 10
for i in range(NUM_PROJETOS):
    controle_projetos.adicionar_projeto(Projeto(i))

controle_projetos.executar()
controle_projetos.imprimir_saldos()
