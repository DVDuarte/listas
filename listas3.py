def somarlistas(lista1, lista2):
    soma = 3 * [0]
    for i in range(3):
        soma[i] = lista1[i] + lista2[i]
    return soma

lista1 = 3 * [0]
lista2 = 3 * [0]

for i in range(3):
    lista1[i] = int(input(f"Digite o {i+1}º número da Lista 1: "))
for i in range(3):
    lista2[i] = int(input(f"Digite o {i+1}º número da Lista 2: "))

print("A soma dos elementos de mesma posição de cada vetor é: ", somarlistas(lista1, lista2))