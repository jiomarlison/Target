n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

lista = []

if (n==1) or (n==2):
    print("1")
else:
    count=3
    lista = [1, 1]
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        lista.append(termo)
        if n in lista:
            print(f'{n} Está na sequencia de Fibonacci')
            print(lista)
            break
        elif termo > n:
            print('Não está na sequencia de Fibonacci')
            break

