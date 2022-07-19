def show_op(lista):
    print()
    print('Tarefa:')
    print(lista)
    print()

def desfazer(lista):
    if len(lista) >= 1:
        lista_backup.append(lista.pop(-1))
    else:
        print('Nada a desfazer')
        return

def refazer(lista_backup):
    if len(lista_backup) >= 1:
        lista.append(lista_backup.pop(-1))
    else:
        print('Nada a refazer')
        return

if __name__ == '__main__':
    lista = []
    lista_backup = []

    while True:
        entrada = input('Digíte uma tarefa ou undo, redo, ls: ')

        if entrada == 'ls':
            show_op(lista)
            continue
        elif entrada == 'undo': #desfazer
            desfazer(lista)
            continue
        elif entrada == 'redo': #refazer
            refazer(lista_backup)
            continue
        else:
            lista.append(entrada)
            continue
