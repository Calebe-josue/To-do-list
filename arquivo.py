from funções import*
from time import sleep
def arquivoExiste(arq):
    try:
        arquivo=open(arq,'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(arq):
    try:
        arquivo=open(arq,'a')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'\nArquivo {arq} criado com sucesso')

    
def ler_arquivo(arq):
    try:
        arquivo=open(arq,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Lista de Tarefas')
        conteudo=arquivo.readlines()
        for i,k in enumerate(conteudo):
            print(f'{i+1} - {k.strip()}')
        if len(conteudo)==0:
            sleep(1)
            print('Lista Vazia')
        else:
            sleep(1)
            arquivo.close()

def adicionar(arq):
    try:
        while True:
            n=str(input('Digite a sua tarefa\n'))
            if not n:
                sleep(1)
                print('Erro!')
            else:
                arquivo=open(arq,'a')
                arquivo.write(n+'\n')
                arquivo.close()
                sleep(1)
                print('Tarefa adicionada com SUCESSO!\n')
                break
    except ValueError:
        sleep(1)
        print('Erro!')


def remover(arq):
    arquivo=open(arq,'r')
    tarefas=arquivo.readlines()
    arquivo.close()

    if not tarefas:
        sleep(1)
        print('Nenhuma tarefa para remover!')
        return

    cabecalho('Lista de Tarefas')
    for i,k in enumerate(tarefas):
        print(f'{i+1} - {k.strip()}')

    try:
        n=int(input('Digite o número da tarefa que deseja remover\n'))
        tarefa_remov=tarefas.pop(n-1)
        sleep(1)
        print('Tarefa Removida!')
    except ValueError:
        sleep(1)
        print('Digite um valor válido')
        return
    except IndexError:
        sleep(1)
        print('Erro! Número de tarefa inválido.')
        return
    
    arquivo=open(arq,'w')
    for tar in tarefas:
        arquivo.write(tar)
    arquivo.close()