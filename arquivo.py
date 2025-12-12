from funções import*
from time import sleep

def arquivoExiste(arq):
    # Verifica se o arquivo existe, retornando valor Booleano.
    try:
        arquivo=open(arq,'r')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(arq):
    #Função que combinada com outra função no programa principal,garante a criação do arquivo .txt
    try:
        arquivo=open(arq,'a')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'\nArquivo {arq} criado com sucesso')

    
def ler_arquivo(arq):
    # Abre o arquivo, enumera ele e mostra tudo isso. Se o arquivo estiver vazio, mostra que está vazio. Logo após fecha o .txt
    try:
        arquivo=open(arq,'r')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Lista de Tarefas')
        conteudo=arquivo.readlines()
        for i,k in enumerate(conteudo):
            print(f'{i+1} - {k.strip()}')
        if len(conteudo)==0:
            print('Lista Vazia!')
        else:
            sleep(1)
            arquivo.close()

def adicionar(arq):
    # Adiciona tarefas a to-do-list.
    n=str(input('Digite a sua tarefa\n'))
    #Verifica se a variável está vazia.
    if not n.strip():
        print('Erro! a tarefa não pode estar vazia.')
    else:
        arquivo=open(arq,'a')
        arquivo.write(n+' '+'[ ]'+'\n')
        arquivo.close()
        sleep(1)
        print('Tarefa adicionada com SUCESSO!\n')
            

def remover(arq):
    #Remove tarefas da to-do-list.
    arquivo=open(arq,'r')
    tarefas=arquivo.readlines()
    arquivo.close()

    if not tarefas:
        #Se o arquivo estiver vazio, não tem tarefas para remover.
        sleep(1)
        print('Nenhuma tarefa para remover!')
        return

    cabecalho('Lista de Tarefas')
    #Faz um cabeçalho e enumera a lista.
    for k,v in enumerate(tarefas):
        print(f'{k+1} - {v.strip()}')


        try:
            #Pede o indice e remove a tarefa pelo metodo pop()
            n=int(input('Digite o número da tarefa que deseja remover\n'))
            tarefa_remov=tarefas.pop(n-1)
            sleep(1)
            print('Tarefa Removida!\n')
            break
        except ValueError:
            #Rejeita se não for inteiro.
            sleep(1)
            print('Valor inválido\n')

        except IndexError:
            #Se o número for maior que o tamanho da lista, logo o indice é inválido.
            sleep(1)
            print('Erro! Número de tarefa inválido.\n')
        
    # Abre, reescreve e fecha o .txt
    arquivo=open(arq,'w')
    for tar in tarefas:
        arquivo.write(tar)
    arquivo.close()


def concluir(arq):
    #Função para concluir tarefas.
    arquivo = open(arq, 'r')
    tarefas = arquivo.readlines()
    arquivo.close()
    if len(tarefas)==0:
        #Se estiver vazio, informa o usuário e retorna ao menu.
        sleep(1)
        cabecalho('To-do-list')
        sleep(1)
        print('Lista Vazia!\n')
        return
    
    try:
        ler_arquivo(arq)
        entrada= input('Digite qual tarefa deseja concluir\n')
        if not entrada:
            print('Erro! você não digitou nada!')
            return
        num=int(entrada)
    except ValueError:
        print('Erro! número inválido.\n')
        return
    except KeyboardInterrupt:
        print('O usuário decidiu encerrar a entrada.\n')
        return
    
    # Verifica se o número existe
    if num < 1 or num > len(tarefas):
        print('Erro! número de tarefa inválido.')
        return
        

    for k, v in enumerate(tarefas):
        if k + 1 == num:
            if '[X]' in v:
                # Se já estiver concluída, mostra o print.
                print('Tarefa já concluída!')
            else:
                # substitui apenas o "[ ]" por "[ X ]"
                tarefas[k] = v.replace('[ ]', '[X]')
                sleep(1)
                print('Tarefa concluída com sucesso!')
            break
    # Abre, reescreve e fecha o arquivo.
    arquivo = open(arq, 'w')
    for tar in tarefas:
        arquivo.write(tar)
    arquivo.close()
