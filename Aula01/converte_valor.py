"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Próxima aula: lista (vetor). Pesquisar em livros, na internet, no YouTube, etc.

- Meet:     vbc-shqr-wxd

- Problema:
- Projete um programa com duas funções:
  A função principal (main) e a função converte em minutos.

  A função converte em minutos recebe dois parâmetros (valores) inteiros que
corresponde ao horário no formato (hora e minuto), faz o cálculo e retorna
um valor inteiro que corresponde ao horário convertido em minutos.
Use variável local.

  A função principal (main) lê o horário (hora e minuto) digitado pelo usuário,
chama a função converte em minutos passando os dois argumentos (hora e minuto)
e com o valor retornado pela função, mostra uma mensagem apropriada, ou seja,
o horário convertido em minutos. Use variável local.

Teste 1: Entrada: horas: 1, minutos: 30         Saída: 90 minutos.
Teste 2: Entrada: horas: 2, minutos: 10         Saída: 130 minutos.  """

def converte_em_minuto(horas, minutos): # Assinatura da função
    """ Converte hh:mm em minutos. """  # docstring
    vl_minutos = horas * 60 + minutos
    return vl_minutos                   # Retorna o valor calculado

# Início do programa principal
if __name__ == '__main__':              # Atalho: mai <tab>
    h = int(input("Horas: "))           # Lê os dados de entrada
    m = int(input("Minutos: "))
    retorno = converte_em_minuto(h, m)  # Chama a função
    print("Horário em minutos:", retorno)

''' --- ALTERAÇÕES:
a. No final do programa principal (main), mostre também o valor da hora 
   e do minuto lidos.
b. Chame a função converte_em_minuto pelo menos duas vezes.
c. Crie a função converte_em_minuto_2, que recebe dois números inteiros
   (hora e minuto) e mostra o valor da conversão. 
   A função não retorna nada.
d. Crie a função le_valor_inteiro. Ela não recebe nada e retorna o
   valor lido. 
   No programa principal, substitua os dois inputs por duas chamadas 
   a função le_valor_inteiro.
    --- Dicas:
    print(h, "horas e", m, "minutos =", retorno, "minutos.")        # a.
    print("{} horas e {} minutos = {} minutos." .format(h, m, retorno))
    print(f"{h} horas e {m} minutos = {retorno} minutos.")
    h = int(input("Horas: "))           # Lê os dados de entrada    # b.
    m = int(input("Minutos: "))
    retorno = converte_em_minuto(h, m)  # No final do main.        
    print(f"{h} horas e {m} minutos = {retorno} minutos.")
def converte_em_minuto_2(horas, minutos): # Assinatura da função    # c.
    vl_minutos = horas * 60 + minutos
    print(f"{horas} horas e {minutos} minutos totalizam {vl_minutos} minutos.")
if __name__ == '__main__':                          
    h = int(input("Horas: "))              # Lê os dados de entrada
    m = int(input("Minutos: "))
    converte_em_minuto_2(h, m)             # Chama a função
def le_valor_inteiro():                                             # d.
    valor = int (input('Digite um valor: '))
    return valor
if __name__ == '__main__':                          # No main           
    # h = int(input("Digite às horas: "))                
    # m = int(input("Digite os minutos: "))
    h = le_valor_inteiro()
    m = le_valor_inteiro()

'''
