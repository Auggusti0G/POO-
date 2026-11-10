"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Projete um programa com duas funções:
  A função principal (main) e a função calcula media.

  A função (def) que calcula a média aritmética de dois valores reais recebe dois
valores reais como parâmetro, calcula a média aritmética e retorna o resultado
do cálculo.

  A função principal (main) lê os dois valores reais digitados pelo usuário,
chama a função passando os valores lidos (os argumentos) e depois mostra o
valor retornado pela função, ou seja, a média aritmética calculada.         """

# Função que calcula a média aritmética
def calcular_media(v1, v2):  # Recebe dois parâmetros
    media = (v1 + v2) / 2    # Cálculo
    return media             # Retorna o valor calculado

# Função principal
if __name__ == '__main__':
    # Leitura dos três valores reais
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    # Chamada da função de média
    resultado = calcular_media(valor1, valor2)
    # Exibição do resultado
    print("A média aritmética é:", resultado)
