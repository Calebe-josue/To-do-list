from time import sleep
from arquivo import*
from funções import*
import os

lista_de_tarefas=Todolist('lista_de_tarefas.json')

if not lista_de_tarefas.arquivoExiste():
    #Verifica se o arquivo existe.Se não existe, cria um novo.
    lista_de_tarefas.criarArquivo()
    
while True:
    sleep(3)
    os.system('cls')
    op=menu(['Visualizar Tarefas','Adicionar Tarefas','Remover tarefas','Concluir tarefas','Histórico de tarefas concluídas','Sair'])
    if op is None:
        continue
    elif op==1:
        #Opção de Visualizar a To-do-list.
        sleep(1)
        lista_de_tarefas.ler_arquivo()
    elif op==2:
        #Opção de adicionar tarefa na To-do-list.
        sleep(1)
        lista_de_tarefas.adicionar()
    elif op==3:
        #Opção de remover tarefa da To-do-list.
        sleep(1)
        lista_de_tarefas.remover()
    elif op==4:
        #Opção de concluir tarefas da to-do-list.
        sleep(1)
        lista_de_tarefas.concluir()
    elif op==5:
        sleep(1)
        lista_de_tarefas.historico()
    elif op==6:
        #Opção de sair do programa.
        sleep(1)
        print('-----FIM DO PROGRAMA-----')
        break
