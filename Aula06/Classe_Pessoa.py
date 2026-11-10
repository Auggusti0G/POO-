"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema (Meet: vbc-shqr-wxd):

- Com base nos conceitos de Programação Orientada a Objetos (POO),
implemente a entidade pessoa com estas características (atributos):

nome,
peso,
altura e
ano de nascimento.

-Implemente:

1- Crie o arquivo .py e a classe Pessoa
2- Crie o método construtor (__init__), ele recebe os parâmetros que serão
   armazenados nos atributos da classe: nome, peso, altura e ano de nascimento
class NomeClasse:                                # Modelo
    def __init__ (self, parametro1, parametro2): # Construtor
        self.atributo1 = parametro1              # Atributos da classe
        self.atributo2 = parametro2
3- No método main, crie (instancie) dois objetos da classe e passe os argumentos
if __name__ == '__main__':            # mai <tab> (tecla de atalho)
    objeto1 = NomeClasse(arg1, arg2)  # Cria (instancia) o primeiro objeto da classe
4- No método main, mostre os objetos criados, teste (rode) a classe
   print("Objeto criado:", objeto1)              # Teste

5- Crie os métodos (defs) gets dos atributos para consultar os dados.
   def get_atributo1(self):           # Modelo do método get (consulta)
       return self.atributo1
6- No main, use (teste) os métodos gets para consultar os objetos criados
   print("Mensagem:", objeto1.get_atributo1())

7- Crie os métodos sets (defs) dos atributos para alterar os dados.
   def set_atributo1(self, novo_valor):  # Modelo do método set (altera)
       self.atributo1 = novo_valor
8- No main, use (teste) os métodos sets para os alterar os objetos criados
   objeto1.set_atributo1("Novo valor")
   print("Mensaggem:", objeto1.get_atributo1()) # verifica se alterou na memória
9- No main, altere o valor do atributo ano de nascimento da pessoa 1 para 2005. Teste

10- Crie o método (def) calcula idade, ele não recebe nada e retorna à idade da pessoa.
    Teste
11- Refaça o método (def) calcula idade usando a biblioteca datetime para
    pegar a data atual do sistema operacional onde o programa está rodando.

"""


import datetime
# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class Pessoa(object):
# class Pessoa():       # Três formas equivalentes de criar a classe.
class Pessoa:
    def __init__(self, nome, peso, altura, ano_nascimento): # Método construtor
        self.nome = nome                                    # Atributos
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento
    def get_nome(self):                     # Método consulta
        return self.nome
    def get_peso(self):
        return self.peso
    def get_altura(self):
        return self.altura
    def get_ano_nascimento(self):
        return self.ano_nascimento

    def set_nome(self, novo_nome):          # Método altera
        self.nome = novo_nome
    def set_peso(self, novo_peso):
        self.peso = novo_peso
    def set_altura(self, nova_altura):
        self.altura = nova_altura
    def set_ano_nascimento(self, novo_ano):  # Altera sem crítica
        self.ano_nascimento = novo_ano

    def calcula_idade(self):                # Método funcional
        hoje = 2025
        idade = hoje - self.ano_nascimento
        return idade

    # def calcula_idade(self):                # Método funcional
    #     hoje = datetime.date.today()        # Data  de hoje (ano, mes, dia)
    #     idade = hoje.year - self.ano_nascimento  # year pega o ano de uma data
    #     return idade                        # Solução incompleta

if __name__ == '__main__':                      # Atalho: mai <tab>
    pessoa1 = Pessoa("Carlos", 71, 1.80, 2000) # Construtor
    print("Objeto criado:", pessoa1)            # Chama o método __str__
    # print anterior: Objeto criado: <pessoa1.Pessoa object at 0x000001BAE4E25A60>
    pessoa2 = Pessoa("Rogerio", 77, 1.82, 1995) # Chama __init__
    print("Objeto criado:", pessoa2)
    # print anterior: Objeto criado: <pessoa1.Pessoa object at 0x000001BAE4E25A90>

    # nome = pessoa1.get_nome()                   # Usando variável
    # print("- Pessoa 1:\nNome:", nome)
    print("- Pessoa 1:\nNome:", pessoa1.get_nome())  # Igual as duas anteriores
    print("Peso:", pessoa1.get_peso())     # Consulta
    print("Altura:", pessoa1.get_altura()) # Consulta
    print("Ano Nascimento:", pessoa1.get_ano_nascimento())  # Direto no print
    print("- Pessoa 2:\nNome:", pessoa2.get_nome())
    print("Peso:", pessoa2.get_peso())     # Consulta
    print("Altura:", pessoa2.get_altura()) # Consulta
    print("Ano Nascimento:", pessoa2.get_ano_nascimento())  # Direto no print

    pessoa1.set_ano_nascimento(2005)
    print("Ano Nascimento alterado:", pessoa1.get_ano_nascimento())  # Confirma

    pessoa1.set_nome("Rogério")                  # Tipo do argumento correto
    print('Nome alterado:', pessoa1.get_nome())  # Teste
    print("- Pessoa 2:\nNome:", pessoa2.get_nome())
    print("Peso:", pessoa2.get_peso())     # Consulta

    print("Idade, pessoa 1:", pessoa1.calcula_idade())
    print("Idade, pessoa 2:", pessoa2.calcula_idade())

