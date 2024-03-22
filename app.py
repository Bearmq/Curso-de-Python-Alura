from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Morango', 5.0, 'grande')
prato_file = Prato('Filé', 10.0, 'O melhor filé da cidade')
restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_file)

def main():
    print(bebida_suco)
    print(prato_file)

if __name__ == '__main__':
    main()