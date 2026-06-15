from datetime import datetime

ATIVA = 1
INATIVA = 2
MANUTENCAO = 3

STATUS = {ATIVA:"Ativa", INATIVA:"Inativa", MANUTENCAO:"Em manutenção"}

def mostrarMenu():
    texto = '''
======================================================
      SISTEMA DE GERENCIAMENTO DE MÁQUINAS
======================================================

1 - Adicionar uma máquina no sistema
2 - Buscar uma máquina no sistema
3 - Listar todas as máquinas do sistema
4 - Atualizar uma máquina
5 - Excluir uma máquina do sistema
6 - Listar máquinas por categoria
7 - Inativar máquinas
0 - Sair do sistema

Escolha uma das opções acima: '''
    
    return texto

def lerData():
    data = input('digite a data de manutenção (dd/mm/aaaa): ')
    return datetime.strptime(data, "%d/%m/%Y").date()

def adicionarMaquina(maquinas, id, nome, marca, modelo, numero_serie, categoria, status, data_manutencao, fabricante):
    maquina = {
            'id': id,
            'nome': nome,
            'marca': marca,
            'modelo': modelo,
            'numero_serie': numero_serie,
            'categoria': categoria,
            'status': status,
            'data_manutencao': data_manutencao,
            'fabricante': fabricante
        }
    maquinas.append(maquina)
    return maquina

def listarMaquinas(maquinas):
    for maquina in maquinas:
        print("=" * 40)
        print('ID:', format(maquina['id']))
        print('Nome:', format(maquina['nome']))
        print('Marca:', format(maquina['marca']))
        print('Modelo:', format(maquina['modelo']))
        print('Número de série:', format(maquina['numero_serie']))
        print('Categoria:', format(maquina['categoria']))
        print('Status: {}'.format(STATUS[maquina['status']]))
        print('Data de manutenção:',maquina['data_manutencao'].strftime("%d/%m/%Y"))
        print('Fabricante:', format(maquina['fabricante']))
        print("=" * 40)


opcao = 1
maquinas =[]
while opcao != 0:
    opcao = int(input(mostrarMenu()))
    if opcao == 1:
        print("\n=== ADICIONAR MÁQUINA ===\n")
        id = int(input('Digite o id da máquina: '))
        nome = input('Digite o nome da máquina: ')
        marca = input('Digite a marca da máquina: ')
        modelo = input('Digite o modelo da máquina: ')
        numero_serie = input('Digite o número de série da máquina: ')
        categoria = input('Digite a categoria da máquina: ')

        print("1 - Ativa")
        print("2 - Inativa")
        print("3 - Em manutenção")
        status = int(input("Digite uma das opções acima para definir o status: "))

        while status < 1 or status > 3:
            print("status invalido!")
            status = int(input("Digite 1, 2 ou 3"))

        data_manutencao = lerData()

        fabricante = input('Digite o fabricante da máquina: ')
        maquina = adicionarMaquina(maquinas, id, nome, marca, modelo, numero_serie, categoria, status, data_manutencao, fabricante)
        print('=== Máquina adicionada com sucesso! ===')

    elif opcao == 2:
        print('Buscar uma máquina no sistema')

    elif opcao == 3:
        print('Listar todas as máquinas do sistema')
        print('\nMÁQUINAS CADASTRADAS NO SISTEMA')
        listarMaquinas(maquinas)

    elif opcao == 4:
        print('Atualizar uma máquina')

    elif opcao == 5:
        print('Excluir uma máquina do sistema')

    elif opcao == 6:
        print('Listar máquinas por categoria')

    elif opcao == 7:
        print('Mudar status')

    elif opcao == 0:
        print('Sair do sistema')

    else:
        print('Opção inválida! \n Digite novamente')