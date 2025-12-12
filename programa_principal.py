from time import sleep
from arquivo import*
from funções import*

arquivo='To-do-list.txt'

if not arquivoExiste(arquivo):
    #Verifica se o arquivo existe.Se não existe, cria um novo.
    criarArquivo(arquivo)
    
while True:
    op=menu(['Visualizar Tarefas','Adicionar Tarefas','Remover tarefas','Concluir tarefas','Sair'])
    if op is None:
        continue
    elif op==1:
        #Opção de Visualizar a To-do-list.
        sleep(1)
        ler_arquivo(arquivo)
    elif op==2:
        #Opção de adicionar tarefa na To-do-list.
        sleep(1)
        adicionar(arquivo)
    elif op==3:
        #Opção de remover tarefa da To-do-list.
        sleep(1)
        remover(arquivo)
    elif op==4:
        #Opção de concluir tarefas da to-do-list.
        sleep(1)
        concluir(arquivo)
    elif op==5:
        #Opção de sair do programa.
        sleep(1)
        print('-----FIM DO PROGRAMA-----')
        break
