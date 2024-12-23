'''
1.Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
2.No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
3.Crie uma nova classe chamada Carro que herda da classe Veiculo.
4.No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
5.Em um arquivo chamado main.py, importe a classe Carro.
6.No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
'''
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 

    @abstractmethod
    def ligar(self):
        pass
        