from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Xan', 11)
restaurante_praca.receber_avaliacao('Louis', 8)
restaurante_praca.receber_avaliacao('Ane', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()