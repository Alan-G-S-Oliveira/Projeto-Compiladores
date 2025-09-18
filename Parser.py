linha = "return (fact((n-1), (a * n)))"

import re

def normalizar_espacos(texto: str) -> str:
    resultado = re.sub(r'\s+', ' ', texto)
    return resultado.strip()

def eliminar_parenteses_externos(linha: str) -> str:
    posicoes_remover = []
    remove = False

    linha = linha.strip()

    aux = linha.split(maxsplit=1)[1]
    if aux[0] == '(':
        posicoes_remover.append(0)
        for i in range(1, len(aux)):
            if aux[i] == '(':
                posicoes_remover.append(i)
            if aux[i] == ')':
                if len(posicoes_remover) == 1 and i != len(aux) - 1:
                    break
                if len(posicoes_remover) == 1 and i == len(aux) - 1:
                    posicoes_remover.append(i)
                    remove = True
                    break
                else:
                    posicoes_remover.pop()

    if remove:
        return "return " + aux[posicoes_remover[0] + 1:posicoes_remover[1]]
    else:
        return linha
    
def eliminar_parenteses_duplicados(linha: str) -> str:
    posicoes_remover = None
    remove = False

    linha = linha.strip()

    for i in range(1, len(linha) - 1):
        if linha[i] == linha[i + 1] == '(' and not(linha[i - 1].isalnum()) and linha[i - 1] != '_':
            posicoes_remover = [i]
        if posicoes_remover != None and linha[i] == linha[i + 1] == ')':
            posicoes_remover.append(i)
            remove = True
            break

    if remove:
        return linha[:posicoes_remover[0]] + linha[posicoes_remover[0] + 1:posicoes_remover[1]] + linha[posicoes_remover[1] + 1:]
    else:
        return linha
    
def eliminar_parenteses_inuteis(linha: str) -> str:
    posicoes_remover = None
    posicoes_removerem = True
    remove = False

    linha = linha.strip()

    #MUDAR
    for i in range(1, len(linha)):
        if linha[i] == '(' and not(linha[i - 1].isalnum()) and linha[i - 1] != '_':
            posicoes_remover = [i]
            posicoes_removerem = True
        elif linha[i] == ')' and posicoes_removerem:
            posicoes_remover.append(i)
            remove = True
            break
        else:
            aux = linha[i]
            if not(aux.isalnum()) and aux != '_' and aux != ' ':
                posicoes_removerem = False

    if remove:
        return linha[:posicoes_remover[0]] + linha[posicoes_remover[0] + 1:posicoes_remover[1]] + linha[posicoes_remover[1] + 1:]
    else:
        return linha
    
print(linha)

while True:
    aux = eliminar_parenteses_externos(linha)
    if aux == linha:
        break
    linha = aux
print(linha)

while True:
    aux = eliminar_parenteses_duplicados(linha)
    if aux == linha:
        break
    linha = aux
print(linha)

while True:
    aux = eliminar_parenteses_inuteis(linha)
    if aux == linha:
        break
    linha = aux
print(linha)

linha = normalizar_espacos(linha)

print(linha)
