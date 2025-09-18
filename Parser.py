linha = 'return func(a, b) + c'

def eliminar_parenteses_1(linha: str) -> str:
    cont = []
    remove = False
    for i in range(len(linha)):
        if linha[i] == '(':
            cont.append(i)
        elif linha[i] == ')':
            if len(cont) == 1 and i != len(linha) - 1:
                break
            if len(cont) == 1 and i == len(linha) - 1:
                cont.append(i)
                remove = True
            else:
                cont.pop()

    if remove:
        return linha[:cont[0]] + linha[cont[0] + 1:cont[1]]
    else:
        return linha
    
def eliminar_parenteses_2(linha: str) -> str:
    cont = None
    remove = False
    for i in range(len(linha) - 1):
        if linha[i] == linha[i + 1] == '(':
            cont = [i]
        if cont != None and linha[i] == linha[i + 1] == ')':
            cont.append(i)
            remove = True
            break

    if remove:
        return linha[:cont[0]] + linha[cont[0] + 1:cont[1]] + linha[cont[1] + 1:]
    else:
        return linha
    
def eliminar_parenteses_3(linha: str) -> str:
    cont = None
    contem = True
    remove = False
    for i in range(len(linha)):
        if linha[i] == '(':
            cont = [i]
            contem = True
        elif linha[i] == ')' and contem:
            cont.append(i)
            remove = True
            break
        else:
            aux = linha[i]
            if not(aux.isalnum()):
                contem = False

    if remove:
        return linha[:cont[0]] + linha[cont[0] + 1:cont[1]] + linha[cont[1] + 1:]
    else:
        return linha
    
while True:
    aux = eliminar_parenteses_1(linha)
    if aux == linha:
        break
    linha = aux
    print('AAA')

while True:
    aux = eliminar_parenteses_3(linha)
    if aux == linha:
        break
    linha = aux
    print('CCC')

print(linha)

while True:
    aux = eliminar_parenteses_2(linha)
    if aux == linha:
        break
    linha = aux
    print('BBB')

print(linha)
