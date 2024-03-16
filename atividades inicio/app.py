import os

# dicionario
restaurantes = [{'nome': 'VidaBoa', 'categoria': 'Japonesa', 'ativo':False},
                {'nome': 'PizzaLoka', 'categoria': 'Pizza', 'ativo':True},
                {'nome': 'LaMassa', 'categoria': 'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    '''Essa função mostra o nome do programa'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Essa função mostra a lista de opções do menu'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função serve para finalizar o programa.
    Extenção pra limpar o terminal'''
    os.system('cls')
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    '''Essa função serve para que a pessoa retorne para o menu principal'''
    input('\nDigite uma tecla para voltar ao menu ')
    main() 

def exibir_subtitulo(texto):
    '''Essa função serve para fazer alterações e exibir o subtitulo'''
    os.system('cls')
    # len de tamanho.
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Essa função serve para quando a pessoa escolher uma opção que n
    esta na lista de opções'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é para cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função serve para listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando os restaurantes') 

    print(f'{' - Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        # ljust vai arrumar o espaçamento
        print(f' - {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função serve para alterar o estado do restaurante'''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função serve para mostrar o menu de opções'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
             listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante = ()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()