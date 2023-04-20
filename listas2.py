def listarvalores(x, y):
    valores = (abs(x-y) + 1) * [0]
    if x == y:
        valores = [x]
        return valores
    else:
        if x < y:
            for i in range(abs(x-y) + 1):
                valores[i] = x
                x = x + 1
            return valores
        else:
            for i in range(abs(y-x) + 1):
                valores[i] = x
                x = x - 1
            return valores

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

print(listarvalores(x, y))