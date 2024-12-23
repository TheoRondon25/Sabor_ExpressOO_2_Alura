from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pao da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_bolo = Sobremesa('Bolo de cenoura', 10.00, 'Bolo de cenoura com cobertura de chocolate', 'Doce', 'Médio')
sobremesa_bolo.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(sobremesa_bolo)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()