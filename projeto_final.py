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
7 - Mudar status da máquina
0 - Sair do sistema

Escolha uma das opções acima: '''
    
    return texto

def lerData():
    data = input('digite a data de manutenção (dd/mm/aaaa): ')
    return datetime.strptime(data, "%d/%m/%Y").date()

def adicionarMaquina(maquinas, id, nome, marca, modelo, numero_serie, categoria, status, data_manutencao):
    maquina = {
            'id': id,
            'nome': nome,
            'marca': marca,
            'modelo': modelo,
            'numero_serie': numero_serie,
            'categoria': categoria,
            'status': status,
            'data_manutencao': data_manutencao
        }
    maquinas.append(maquina)
    return maquina

def buscarMaquina(maquinas, busca):
    if len(maquinas) == 0:
        print("Nenhuma máquina cadastrada!")
        return

    for maquina in maquinas:
        if busca == maquina['id']:
            print("ID: {}".format(maquina['id']))
            print("Nome: {}".format(maquina['nome']))
            print("Marca: {}".format(maquina['marca']))
            print("Modelo: {}".format(maquina['modelo']))
            print("Número de série: {}".format(maquina['numero_serie']))
            print("Categoria: {}".format(maquina['categoria']))
            print("Status: {}".format(STATUS[maquina['status']]))
            print("Data de manutenção: {}".format(
                maquina['data_manutencao'].strftime("%d/%m/%Y")
            ))
            return

    print("Máquina não encontrada!")

def listarMaquinas(maquinas):
    if len(maquinas) == 0:
        print("Nenhuma máquina cadastrada!")
        return
    for maquina in maquinas:
        print("=" * 40)
        print('ID:', format(maquina['id']))
        print('Nome:', format(maquina['nome']))
        print('Marca:', format(maquina['marca']))
        print('Modelo:', format(maquina['modelo']))
        print('Número de série:', format(maquina['numero_serie']))
        print('Categoria:', format(maquina['categoria']))
        print("Status:", format(STATUS[maquina['status']]))
        if hasattr(maquina['data_manutencao'], 'strftime'):
            data_manutencao = maquina['data_manutencao'].strftime("%d/%m/%Y")
        else:
            data_manutencao = maquina['data_manutencao']
        print('Data de manutenção:', data_manutencao)
        print("=" * 40)

def atualizarMaquina(maquinas, busca, nome, marca, modelo, numero_serie, categoria, data_manutencao):
    if len(maquinas) == 0:
        print("Nenhuma máquina cadastrada!")
        return

    for maquina in maquinas:
        if busca == maquina['id']:
            maquina['nome'] = nome
            maquina['marca'] = marca
            maquina['modelo'] = modelo
            maquina['numero_serie'] = numero_serie
            maquina['categoria'] = categoria
            maquina['data_manutencao'] = data_manutencao

            print("Máquina atualizada com sucesso!")
            return

    print("Máquina não encontrada!")

def excluirMaquina(maquinas, busca):
    if len(maquinas) == 0:
        print("Nenhuma máquina cadastrada!")
        return

    for maquina in maquinas:
        if busca == maquina['id']:
            maquinas.remove(maquina)
            print("Máquina excluída com sucesso!")
            return

    print("Máquina não encontrada!")

def mudarStatus(maquinas, busca, status):
    if len(maquinas )== 0:
        print("Nenhuma máquina cadastrada!")
        return
    
    for maquina in maquinas:
        if busca == maquina['id']:
            maquina['status'] = status
            print("Status alterado com sucesso!")
            return
        
    print('Máquina não encontrada!')

def salvarMaquinaEmArquivo(maquinas):
    arquivo = open("dados/dados.txt", 'w')
    for maquina in maquinas:
        arquivo.write("{};".format(maquina['id']))
        arquivo.write("{};".format(maquina['nome']))
        arquivo.write("{};".format(maquina['marca']))
        arquivo.write("{};".format(maquina['modelo']))
        arquivo.write("{};".format(maquina['numero_serie']))
        arquivo.write("{};".format(maquina['categoria']))
        arquivo.write("{};".format(maquina['status']))
        arquivo.write("{}\n".format(maquina['data_manutencao'].strftime('%d/%m/%Y')))

def lerDados(maquinas):
    id = 0
    arquivo = open("dados/dados.txt", 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        if linha.strip()=="":
            continue
        palavras = linha.split(';')
        maquina = {}
        maquina['id'] = int(palavras[0])
        id = int(palavras[0])
        maquina['nome'] = palavras[1]
        maquina['marca'] = palavras[2]
        maquina['modelo'] = palavras[3]
        maquina['numero_serie'] = palavras[4]
        maquina['categoria'] = palavras[5]
        maquina['status'] = int(palavras[6])
        maquina['data_manutencao'] = datetime.strptime(palavras[7].strip(),"%d/%m/%Y").date()
        maquinas.append(maquina)
    return (id + 1)
            
opcao = 1
maquinas = []
cont = lerDados(maquinas)

while opcao != 0:
    opcao = int(input(mostrarMenu()))
    if opcao == 1:
        print("\n=== ADICIONAR MÁQUINA ===\n")
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

        maquina = adicionarMaquina(maquinas, cont, nome, marca, modelo, numero_serie, categoria, status, data_manutencao)
        print('=== Máquina adicionada com sucesso! ===')

        cont += 1

    elif opcao == 2:
        print('\n=== BUSCAR MÁQUINA ===\n')
        busca = int(input("Digite o id da máquina: "))
        buscarMaquina(maquinas, busca)

    elif opcao == 3:
        print('\n=== LISTAR MÁQUINAS ===\n')
        listarMaquinas(maquinas)

    elif opcao == 4:
        print('\n=== ATUALIZAR MÁQUINA ===\n')
        busca = int(input("Digite o id da máquina a ser atualizada: "))
        nome = input("Digite o nome: ")
        marca = input("Digite a marca: ")
        modelo = input("Digite o modelo: ")
        numero_serie = input("Digite o número de série: ")
        categoria = input("Digite a categoria: ")
        data_manutencao = lerData()
         
        atualizarMaquina(maquinas, busca, nome, marca, modelo, numero_serie, categoria, data_manutencao)

    elif opcao == 5:
        print('\n=== EXCLUIR MÁQUINA ===\n')
        busca = int(input("Digite o id da máquina a ser excluida: "))
        excluirMaquina(maquinas, busca)

    elif opcao == 6:
        print('Listar máquinas por categoria')

    elif opcao == 7:
        print("=== MUDAR STATUS ===")
        busca = int(input("Digite o id da máquina: "))

        print("1 - Ativa")
        print("2 - Inativa")
        print("3 - Em manutenção")

        status = int(input("Digite o novo status: "))

        while status < 1 or status > 3:
            print("Status inválido!")
            status = int(input("Digite 1, 2 ou 3: "))

        mudarStatus(maquinas, busca, status)

    elif opcao == 0:
        salvarMaquinaEmArquivo(maquinas)
        print('Sair do sistema')
        
    else:
        print('Opção inválida! \n Digite novamente')