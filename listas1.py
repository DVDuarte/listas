def calcularMedia(notas):
    total = 0
    for i in range(len(notas)):
        total = total + notas[i]
    media = total/len(notas)
    return media

notas = 5 * [0]

for i in range(len(notas)):
    notas[i] = int(input(f"Digite a {i+1}ª nota: "))

print(calcularMedia(notas))