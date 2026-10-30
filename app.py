import os # Modulo para interagir com o sistema operacional

carros = [{'nome' : 'mustang', 'marca' : 'Ford', 'ano' : '1978', 'ativo' : False},
          {'nome' : 'Civic', 'marca': 'Honda','ano': '2008', 'ativo' : True},
          {'nome' : 'Corsa', 'marca': 'Chevrolet', 'ano' : '1998', 'ativo' : False}]

def exibir_nome_do_programa():
    ''' Exibir o título do aplicativo na tela '''
    # Para exibir uma informção para usuário, utilizamos a função print().
    print("Táxi Express\n")

def exibir_opcoes():
    ''' Exibir as funcionalidades do aplicativo no menu principal'''
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Desativar/Ativar carro")
    print("4. Sair")

def finalizar_app():
    ''' Exibir mensagem de finalização do aplicativo'''
    exibir_subtitulo('Finalizando o app')

def opção_invalida():
    '''
    Exibir uma mensagem de opção inválida e retorna para menu principal

    Outputs:
    - retorna ao menu principal
    
    '''
    print("\nOpção Inválida")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    '''
    Exibindo um subtítulo estilizado na tela

    Inputs:
    - texto: str - O texto substítulo
    '''
    os.system('cls')
    linha = '-'* len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_carro():
    '''
    Uma função responsável por cadastrar um novo carro

    Inputs:
    -Nome do carro
    -Marca do carro
    -Ano do carro

    Outputs:
    -Adiciona um novo carro a lista de carros
    '''
    exibir_subtitulo('Cadastro de novos carros')

    nome_carro = input('Digite o nome do carro que deseja cadastrar: ')
    marca_carro =  input(f'Digite a marca do {nome_carro}: ')
    ano_carro = input(f'Digite o ano do {nome_carro}: ')
    dados_carro = {'nome' : nome_carro, 'marca' : marca_carro, 'ano': ano_carro, 'ativo': False}

    carros.append(dados_carro)

    print(f'O Carro {nome_carro} cadastrado com sucesso')
    voltar_menu_principal()

def listar_carros():
    '''
    Uma função para listar todos os carros presenta na lista

    Outputs:
    - Exibi a lista de carros na tela
    '''
    exibir_subtitulo('Listando todos os carros')

    print(f'{'Nome do Carro'.ljust(18)} | {'Marca'.ljust(15)} | {'Ano'.ljust(15)} | Status')
    for carro in carros:
        nome_carro = carro['nome']
        marca_carro = carro['marca']
        ano_carro = carro['ano']
        ativo_carro = 'ativado' if carro['ativo'] else 'desativado' #Ternario
        print(f' - {nome_carro.ljust(15)} | {marca_carro.ljust(15)} | {ano_carro.ljust(15)} | {ativo_carro.ljust(15)}')
    
    voltar_menu_principal()

def voltar_menu_principal():
    '''
    Solicita uma tecla para voltar para menu principal

    Outputs:
    -Retorna ao menu principal
    '''
    input("\nDigite uma tecla para voltar no menu: ")
    main()

def ativando_carro():
    '''
    Uma função para Ativar/Desativar o status de um carro

    Outputs:
    -Exibe uma mensagem indicando o sucesso da operação

    '''
    exibir_subtitulo('Alterando o status do carro')

    nome_carro = input('Digite o nome do carro que deseja alterar o status: ')
    
    for carro in carros:
        if nome_carro == carro['nome']:
            carro_encontrado = True
            carro['ativo'] = not carro['ativo'] #not inver a oposição da variavel, se tiver True vai para false e se tiver False vai para True
            mensagem = f'O carro {nome_carro} foi ATIVADO com sucesso' if carro['ativo'] else f'O carro {nome_carro} foi DESATIVADO com sucesso'
            print(mensagem)

    if not carro_encontrado:
        print(f'O carro {nome_carro} não foi encontrado')

    voltar_menu_principal()

def escolher_opcao_match():
    '''
    Solicita e executa a opção escolhida pelo usuário

    Outputs: 
    - Executa a opção escolhida pelo usuário
    '''
    #Utilizando o try e except, para tratamento de erro, como o usuario pode digitar uma string e o programa está esperando uma entrada Int

    try:
        opcao_escolhida = int(input("Digite a opção que você deseja: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_carro()
            case 2:
                listar_carros()
            case 3:
                ativando_carro()
            case 4:
                finalizar_app()
            case _:   
                opção_invalida()
    except:
        opção_invalida()



def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao_match()


if __name__ == "__main__":
    main()

