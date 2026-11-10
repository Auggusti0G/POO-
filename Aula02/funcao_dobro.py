"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

# Exemplo básico – soma de dois números

- Problema:

- Crie uma função que receba um valor e retorne o dobro do valor,
resulva usando função tradicional.
- No main, leia o valor, chame a função passando o valor lido e
mostre o resultado.

"""
# 1. Função tradicional
def dobro(x):
    calculo = x * 2
    return calculo
if __name__ == '__main__':
    valor = int(input("Valor: "))
    print("Resultado:", dobro(valor))       # Solução 1
    print("Resultado:", dobro(3))           # Solução 2
    # Resultado: 6

""" --- Alterações:
a. Refaça o exercicio usando a função lambda equivalente
    --- Dicas:
- Sintaxe
nome_variavel = lambda argumentos : expressão

dobro = lambda x: x * 2             # Função lambda

if __name__ == '__main__':
    valor = int(input("Valor: "))
    print("Resultado:", dobro(valor))       # Solução 1
    print("Resultado:", dobro(3))           # Solução 2
    # Resultado: 6

"""