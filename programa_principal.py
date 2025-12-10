from time import sleep
from arquivo import*
from funções import*

arquivo='To-do-list'

if not arquivoExiste(arquivo):
    #Verifica se o arquivo existe.Se não existe, cria um novo.
    criarArquivo(arquivo)
    
while True:
    op=menu(['Visualizar Tarefas','Adicionar Tarefa','remover tarefa','Sair'])
    if op==1:
        #Opção de Visualizar a To-do-list
        sleep(1)
        ler_arquivo(arquivo)
    if op==2:
        #Opção de adicionar tarefa na To-do-list
        sleep(1)
        adicionar(arquivo)
    if op==3:
        #Opção de remover tarefa da To-do-list
        sleep(1)
        remover(arquivo)
    if op==4:
        #Parar o programa
        sleep(1)
        print('------FIM DO PROGRAMA-----')
        break

