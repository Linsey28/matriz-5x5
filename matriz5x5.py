matriz = [[0 for _ in range(5)] for _ in range(5)]

print("Registro de Números Terminados en 5: ")

for i in range(5):
    for j in range(5):

        numero = 0
        while numero % 10 != 5:
            numero = int(input(f"Ingrese número para [{i}][{j}] (debe terminar en 5): "))
            if numero % 10 != 5:
                print("Dato inválido. Intente de nuevo.")
        
        matriz[i][j] = numero

print("\nMatriz 5x5 Resultante:")
for fila in matriz:
    for valor in fila:
        print(valor, end="\t")
    print() 