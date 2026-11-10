"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:
- Projete um programa com duas funções:
a função principal (main) e a função valor absoluto.

- Elabore a função (def) valor absoluto que recebe um parâmetro (número)
qualquer e retorna o valor absoluto (módulo) correspondente.

-  A função principal (main) lê o número digitado pelo usuário, chama a
função valor absoluto passando o número lido e depois gera a tela de saída
com o valor retornado pela função valor absoluto.

  Lembrando que o valor absoluto de um número positivo é ele mesmo e
o valor absoluto de um número negativo é ele multiplicado por -1.
- Obs.: não use a função nativa (pronta) da linguagem Python.

Teste 1: valor = 3.0              Saída: Valor absoluto: 3.0
Teste 2: valor = -3.0             Saída: Valor absoluto: 3.0
"""

# A função recebe um parâmetro (valor) e retorna o valor absoluto dele
def valor_absoluto(v):          # Assinatura da função
    if v < 0:
        vlr_absoluto = -v       # vlr_absoluto = -1 * v
    else:
        vlr_absoluto = v
    return vlr_absoluto         # Retorna o valor absoluto para o main
    # Fim da função valor_absoluto.
if __name__ == '__main__':      # Atalho: main <tab>
    valor = float(input("Digite um numero: "))  # Indentação obrigatória.
    retorno = valor_absoluto(valor)  # Valor digitado é passado para a função
    # A variável retorno recebe o valor retornado pela função (def)
    print('Valor absoluto:', retorno)  # Imprime o valor retornado
''' --- ALTERAÇÕES:
a. No main, mostre (imprima) o valor retornado sem usar a variável 'retorno'
b. Refaça a função valor_absoluto usando o if sem o else e sem o elif.
c. Refaça a função sem usar o if ... else
d. Resolva usando a função nativa do Python que tem a mesma funcionalidade.
    --- DICAS ABAIXO:
    # retorno = valor_absoluto(valor)                               # a. 
    # print('Valor absoluto: ', retorno)                    
    print('Valor absoluto:', valor_absoluto(valor))
def valor_absoluto(v):                                              # b.
    if v < 0:                                                                   
        v = -v      # v = -1 * v
    return v                               
def valor_absoluto(v):                                              # c.
    v = v ** 2                  # Solução 1
    v = v ** (1/2)
    return v                    
    return (v ** 2) ** (1/2)    # Solução 2
No main:                                                            # d.
    ...
    # print(valor_absoluto(valor))  # Não chama a função def
    print(abs(valor))               # Chama a função nativa do Python

'''
