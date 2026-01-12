from funções import*
from time import sleep
import json


def arquivoExiste(arq):
    try:
        with open(arq,'r') as arquivo:
            return True
    except (FileNotFoundError):
        return False


def criarArquivo(arq):
    try:
        dados = {"tarefas":[],
                "concluidas":[]
        }
        with open(arq,'w',encoding='utf-8') as arquivo:
            json.dump(dados,arquivo,indent=4)
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'\nArquivo {arq} criado com sucesso')

def carregar_dados(arq):
    with open(arq,'r',encoding='utf-8') as arquivo:
        return json.load(arquivo)


def salvar_dados(dados,arq):
    with open(arq,'w',encoding='utf-8') as arquivo:
        json.dump(dados,arquivo,indent=4)


def ler_arquivo(arq):
    dados = carregar_dados(arq)
    cabecalho('Lista de Tarefas')
    if len(dados['tarefas'])==0:
        print('Lista Vazia!')
        return
    for i,k in enumerate(dados["tarefas"]):
        print(f'{i+1} - {k}')
        

def adicionar(arq):
    n=str(input('Digite a sua tarefa\n'))
    if not n.strip():
        print('Erro! a tarefa não pode estar vazia.')
    else:
        dados = carregar_dados(arq)
        dados['tarefas'].append(n)
        salvar_dados(dados,arq)
        sleep(1)
        print('Tarefa adicionada com SUCESSO!\n')
            

def remover(arq):
    dados = carregar_dados(arq)
    if not dados["tarefas"]:
        sleep(1)
        print('Nenhuma tarefa para remover!')
        return

    cabecalho('Lista de Tarefas')
    for k,v in enumerate(dados['tarefas']):
        print(f'{k+1} - {v.strip()}')

    try:
        n=int(input('Digite o número da tarefa que deseja remover\n'))
        dados['tarefas'].pop(n-1)
        sleep(1)
        print('Tarefa Removida!\n')
    except (ValueError, IndexError):
        sleep(1)
        print('Valor inválido\n')

    salvar_dados(dados,arq)


def concluir(arq):
    dados = carregar_dados(arq)
    if not dados["tarefas"]:
        sleep(1)
        cabecalho('To-do-list')
        sleep(1)
        print('Lista Vazia!\n')
        return
    ler_arquivo(arq)
    try:
        entrada= input('Digite qual tarefa deseja concluir\n')
        if not entrada:
            print('Erro! você não digitou nada!')
            return
        num=int(entrada)
    except (ValueError, IndexError):
        print('Erro! número inválido.\n')
        return
    except KeyboardInterrupt:
        print('O usuário decidiu encerrar a entrada.\n')
        return
    
    if num < 1 or num > len(dados["tarefas"]):
        print('Erro! número de tarefa inválido.')
        return
        
    if dados['tarefas'][num-1] in dados['concluidas']:
        print('Tarefa já concluída!')
    else:
        dados['concluidas'].append(dados["tarefas"][num-1])
        dados['tarefas'].pop(num-1)
        sleep(1)
        print('Tarefa concluída com sucesso!')
    salvar_dados(dados,arq)


def historico(arq):
    dados = carregar_dados(arq)
    if not dados["concluidas"]:
        print('Nenhuma tarefa concluida!')
        return
    for i,k in enumerate(dados['concluidas']):
        print(f'{i+1} - {k}')