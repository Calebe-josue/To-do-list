from time import sleep
def leiaint(msg):
    try:
        a=int(input(msg))
    except (ValueError,TypeError):
        print('Digite um número inteiro válido')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar nada')
        return 0
    else:
        return a


def linha(tam=42):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    sleep(1)
    cabecalho('To-do-List')
    c=1
    for i in lista:
        print(f'{c} - {i}')
        c+=1
    print(linha())
    opc=leiaint('Digite sua opções\n')
    return opc