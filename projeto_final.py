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

def salvarMaquinaEmArquivo(maquinas):
    with open("dados/dados.txt", 'w', encoding='utf-8') as arquivo:
        for maquina in maquinas:
            arquivo.write(f"ID: {maquina['id']}\n")
            arquivo.write(f"Nome: {maquina['nome']}\n")
            arquivo.write(f"Marca: {maquina['marca']}\n")
            arquivo.write(f"Modelo: {maquina['modelo']}\n")
            arquivo.write(f"Numero Serie: {maquina['numero_serie']}\n")
            arquivo.write(f"Categoria: {maquina['categoria']}\n")
            arquivo.write(f"Status: {maquina['status']}\n")
            arquivo.write(f"Data Manutenção: {maquina['data_manutencao'].strftime('%d/%m/%Y')}\n")
            arquivo.write('-' * 30 + '\n')


def listarMaquinas(maquinas):
    for maquina in maquinas:
        print("=" * 40)
        print('ID:', format(maquina['id']))
        print('Nome:', format(maquina['nome']))
        print('Marca:', format(maquina['marca']))
        print('Modelo:', format(maquina['modelo']))
        print('Número de série:', format(maquina['numero_serie']))
        print('Categoria:', format(maquina['categoria']))
        print("Status:", STATUS[maquina['status']])
        if hasattr(maquina['data_manutencao'], 'strftime'):
            data_manutencao = maquina['data_manutencao'].strftime("%d/%m/%Y")
        else:
            data_manutencao = maquina['data_manutencao']
        print('Data de manutenção:', data_manutencao)
        print("=" * 40)
        
def lerDados():
    maquinas = []
    try:
        with open("dados/dados.txt", 'r', encoding='utf-8') as arquivo:
            bloco = {}
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                if linha.startswith('-'):
                    if bloco:
                        maquina = {
                            'id': int(bloco.get('ID', 0)),
                            'nome': bloco.get('Nome', ''),
                            'marca': bloco.get('Marca', ''),
                            'modelo': bloco.get('Modelo', ''),
                            'numero_serie': bloco.get('Numero Serie', ''),
                            'categoria': bloco.get('Categoria', ''),
                            'status': int(bloco.get('Status', ATIVA)),
                            'data_manutencao': datetime.strptime(bloco.get('Data Manutenção', '01/01/1900'), '%d/%m/%Y').date()
                        }
                        maquinas.append(maquina)
                        bloco = {}
                    continue

                chave, valor = linha.split(':', 1)
                bloco[chave.strip()] = valor.strip()

            if bloco:
                maquina = {
                    'id': int(bloco.get('ID', 0)),
                    'nome': bloco.get('Nome', ''),
                    'marca': bloco.get('Marca', ''),
                    'modelo': bloco.get('Modelo', ''),
                    'numero_serie': bloco.get('Numero Serie', ''),
                    'categoria': bloco.get('Categoria', ''),
                    'status': int(bloco.get('Status', ATIVA)),
                    'data_manutencao': datetime.strptime(bloco.get('Data Manutenção', '01/01/1900'), '%d/%m/%Y').date()
                }
                maquinas.append(maquina)
    except FileNotFoundError:
        return []
    return maquinas
        
        
        


opcao = 1
maquinas = lerDados()
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

        maquina = adicionarMaquina(maquinas, id, nome, marca, modelo, numero_serie, categoria, status, data_manutencao)
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
        salvarMaquinaEmArquivo(maquinas)

    else:
        print('Opção inválida! \n Digite novamente')