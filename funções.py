from time import sleep
def leiaint(msg):
    try:
        a = int(input(msg))
        return a  # Retorna o número válido
    except (ValueError, TypeError):
        return None  # Retorna None caso o input seja inválido
    except KeyboardInterrupt:
        return None


def linha(tam=42):
    #Cria linhas
    return '-' * tam


def cabecalho(msg):
    #Cria um cabeçalho com o texto e retorna tudo isso.
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    while True:
        #Faz todo um menu enumerado e retorna isso.
        sleep(1)
        cabecalho('To-do-List')
        for c, i in enumerate(lista, start=1):
            print(f'{c} - {i}')
        print(linha())

        opc = leiaint('Digite sua opção: ')
        
        if opc is None:
            # Se a opção for inválida, mostra erro e retorna para o menu
            print('Erro! Índice inválido. Voltando ao menu...\n')
            continue  # Retorna ao menu se houver erro
        
        if 1 <= opc <= len(lista):
            return opc  # Se a opção for válida, retorna o número
        else:
            print('Erro! Índice inválido. Voltando ao menu...\n')
