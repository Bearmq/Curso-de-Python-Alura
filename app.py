from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Morango', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_file = Prato('Filé', 10.0, 'O melhor filé da cidade')
prato_file.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_file)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()