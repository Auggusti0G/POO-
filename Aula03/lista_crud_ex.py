"""            Comentários de várias linhas     -     Prof. Barbosa
Dicas: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- O que significa CRUD?
- CRUD (acrônimo do inglês Create, Read, Update and Delete) são as
  quatro operações básicas (inclui, consulta, atualiza e apaga os dados)
  utilizadas em bases de dados relacionais (RDBMS) fornecidas aos usuários
  do sistema.

- Desenvolva o programa para simular um CRUD usando lista com as funções:
  main com repetição,
  menu,
  create,
  read,
  update e
  delete.
  Obs.: neste exercício, use nome de pessoas na lista.
1- A função main gerencia o programa usando uma estrutura de repetição,
  ou seja, todas as funções serão chamadas da função main.

2- A função menu não recebe nada (parâmetro), apresenta as quatro operações
   do CRUD, lê a opção digitada pelo usuário e retorna a opção digitada para
   função main:
    [c] - Create (inserir um item)
    [r] - Read (mostrar toda a lista)
    [u] - Update (substituir um item)
    [d] - Delete  (remover um item)
    [e] - Exit (sair)
    Opção:

3- A função create não recebe nada (parâmetro) e não retorna nada (sem return).
   Lê um nome digitado pelo usuário e insere no final da lista.
4- A função read não recebe nada (parâmetro) e não retorna nada (sem return).
   Mostra todos os itens da lista na horizontal.
5- A função update não recebe nada (parãmetro) e não retorna nada (sem return).
   Lê os dados necessários para atualizar (índice e o novo nome) e substituir
   (alterar) um item da lista.
6- A função delete não recebe nada (parâmetro) e não retorna nada (sem return).
   Lê o item (nome) que será removido (excluído) da lista.

Prof. Barbosa

"""
#---------------------------------------------------------------------------
#----------------------------Mostrando o Codigo-----------------------------
#---------------------------------------------------------------------------


l_nomes = []        # Lista vazia, variável global (todas as funções usam)
def menu():
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    opcao = input('Opção: ')
    return opcao
def create():
    nome = input('Inserir - Nome: ')
    l_nomes.append(nome)
def read():
    print("Valores da lista na horizontal:")
    print(l_nomes)                # Na horizontal
def update():
    indice = int(input("Atualizar - Qual posição (índice): "))
    novo_nome = input("Atualizar - Novo nome: ")
    # Usando notação de vetor:  Sintaxe: nome_lista[indice] = novo_nome
    l_nomes[indice] = novo_nome          # Solução 1, notação vetor.
    # l_nomes.pop(indice)                # Solução 2, funções de lista.
    # l_nomes.insert(indice, novo_nome)  # Solução 2
def delete():
    nome = input("Remover - Nome: ")
    l_nomes.remove(nome)
if __name__ == '__main__':  # Atalho: mai <tab>
    while True:  # Solução 2
        op = menu()  # A variável op recebe o valor da função menu
        if op == 'c':
            create()  # Chama a função create
        elif op == 'r':
            read()  # Chama a função read
        elif op == 'u':
            update()  # Chama a função update
        elif op == 'd':
            delete()  # Chama a função delete
        else:
            break

"""
def create():                             # Original
    n = input('Nome: ')
    lista.append(n)

- Alteração a função create:
- Permitir que o usuário digite vários nomes, digite a tecla "enter" para
sair do create
- Dica: estrutura de repetição.

--- Dicas:

def create():
    while True:
        n = input('Nome: ')
        if n == "":             # Enter
            break
        l_nomes.append(n)

---

    # - Solução 2:
    funcao = {'c': create, 'r': read, 'u': update, 'd': delete}  # Dicionário
    while True:
        op = menu()             # A variável op recebe o valor da função menu
        if op in ('c', 'r', 'u', 'd'):
            funcao[op]()
        else:
            break

"""


