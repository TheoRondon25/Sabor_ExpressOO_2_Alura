'''
1.Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
2.Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro
e imprima essas instâncias.
3.Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar
e imprima se o livro está disponível ou não.
4.Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
5.Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
6.No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
7.No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
'''

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

    def __str__(self):
        return f'Título do livro: {self._titulo} | Autor: {self._autor} | Ano de publicação: {self._ano_publicado} | Disponível: {self._disponivel}'

    @classmethod
    def emprestar(cls, emprestado):
        emprestado._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [str(livro) for livro in Livro.livros if livro._ano_publicado == ano and livro._disponivel]
        return livros_disponiveis


livro1 = Livro('Harry Potter', 'J. K. Rowling', 1997)
livro2 = Livro('Livro do Theo', 'Theo Rondon', 2024)
# Livro.emprestar(livro1)
print(livro1)
print(livro2)

Livro.livros = [livro1, livro2]
# print(Livro.verificar_disponibilidade(2024))

# -------------------------------------------

# '''
# 1.Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
# 2.Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
# 3.Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
# '''

# class ContaBancaria:

#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#         self._ativo = False

#     def __str__(self):
#         return f'Olá, {self.titular}! Seu saldo atual é de {self.saldo} reais'

#     @classmethod
#     def ativar_conta(cls, conta):
#         conta._ativo = True

# conta1 = ContaBancaria('Theo', 1000)
# conta2 = ContaBancaria('Taina', 5000)
# print(conta1)
# print(conta2)
# print(f'Conta ativa? {conta1._ativo}')
# ContaBancaria.ativar_conta(conta1)
# print(f'Após ativação = conta ativa? {conta1._ativo}')

# -------------------------------------------

# '''Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método
# especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado
# aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma
# mensagem de saudação personalizada com base na profissão da pessoa.'''

# class Pessoa:

#     def __init__(self, nome, idade, profissao):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao

#     def __str__(self):
#         return f'Olá {self.nome}!!'

#     def aniversario(self):
#         self.idade += 1
#         print(self.idade)

#     @property
#     def saudacao(self):
#         return f'Que ótimo saber que você é um(a) {self.profissao}!'

# pessoa1 = Pessoa('Theo', 20, 'Programador')
# print(pessoa1)
# pessoa1.aniversario()
# print(pessoa1.saudacao)

# -------------------------------------------

# '''Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores
# aos seus atributos através de um método construtor.'''

# class Cliente():
#     def __init__(self, nome, idade, sexo):
#         self.nome = nome
#         self.idade = idade
#         self.sexo = sexo
#         self.status = False

#     def mostrar_dados(self):
#         situacao = 'Inativo'
#         if self.status:
#             situacao = 'Ativo'
#         print(f'Nome: {self.nome} / Idade: {self.idade} / Sexo: {self.sexo} / Status: {situacao}')

# cliente1 = Cliente('Theo', 20, 'M')
# cliente1.status = True

# cliente2 = Cliente('Taina', 20, 'F')

# cliente1.mostrar_dados()
# cliente2.mostrar_dados()

# -------------------------------------------

# """Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos."""

# class Carro():
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano

#     def __str__(self):
#         return f'MODELO: {self.modelo} | COR: {self.cor} | ANO: {self.ano}'

# carro1 = Carro('Camionete', 'Branca', 2018)
# print(carro1)

# -------------------------------------------

# class Musica:

#     def __init__(self, nome, artista, duracao=0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao

# musica1 = Musica('New Years Day', 'U2')

# # print(vars(musica1))
# print(f'Musica: {musica1.nome} - Banda: {musica1.artista} - Duração: {musica1.duracao} segundos')