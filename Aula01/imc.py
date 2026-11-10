##----------------------------------
#---------AULA 01-------------------
#-----------------------------------

"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:
- Desenvolva uma função para calcular o Índice de Massa Corporal (IMC) de
uma pessoa, a função recebe dois parâmetros: o peso em quilogramas e a
altura em metros. E a função retorna o IMC calculado a partir da fórmula,
ou seja, o IMC é igual ao peso dividido pela altura ao quadrado:

- Fórmula:
IMC = _____peso_____
      altura . altura

  A função principal (main) lê o valor do peso e da altura digitado pelo
usuário, chama a função passando os dois valores digitados e mostra o valor
retornado pela função. No main, chame a função pelo menos duas vezes.

Teste 1: Peso: 80 e Altura: 1.7         Saída: IMC = 27.68166089965398

"""

def calcula_imc(peso, altura):
    imc = peso / pow(altura, 2)         # Solução 1
    # imc = peso / (altura ** 2)        # Solução 2
    # imc = peso / (altura * altura)    # Solução 3
    # imc = peso / altura * altura      # Errado
    return imc

if __name__ == '__main__':
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    resultado = calcula_imc(peso, altura)
    print("O IMC é:", resultado)

"""
--- Alterações:
a. Refaça sem usar a variável resultado no main
b. Chame a função pelo menos duas vezes.
c. Refaça usando outras formas de calcular a potência

"""