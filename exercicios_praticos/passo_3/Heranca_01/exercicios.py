# --------------------------------
'''
    1.Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. 
A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
    2.Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
    3.Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas 
que indica a quantidade de portas do carro.
    4.Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e 
inclua a informação sobre a quantidade de portas do carro.
    5.Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, 
indicando se a moto é esportiva ou casual.
    6.Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e 
inclua a informação sobre o tipo da moto.
    7.Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
    8.Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e 
Moto com diferentes marcas, modelos, quantidade de portas e tipos.
    9.Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
'''
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
    
    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Ligado: {status}'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Ligado: {status} | Portas: {self.portas}'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Ligado: {status} | Tipo: {self.tipo}'
    