#importando biblioteca randômica

import random
#definir o tamanho da matriz
TAM = 3
#Definido um laço para a matriz que 
# intera TAM vezes
mat = [[] for _ in range(TAM)]

#Entrada de valores randômicos
for lin in range(TAM):
    for col in range(TAM):
        mat[lin].append(random.randrange(0,10))

#Saída de dados
print("Matriz:")
for cont in mat:
    print(cont)

#processamento
print(f"Diagonal Principal: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin==col:
            print(f" {mat[lin][col]}")

print(f"Triângulo Superior Diagonal Principal: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin<col:
            print(f" {mat[lin][col]}")

print(f"Triângulo Inferior Diagonal Principal: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin>col:
            print(f" {mat[lin][col]}")

print(f"Diagonal Secundária: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin+col==TAM-1:
            print(f"{ mat[lin][col]}")

print(f"Triângulo Superior Diagonal Secundária: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin+col<TAM-1:
            print(f" {mat[lin][col]}")

print(f"Triângulo Inferior Diagonal Secundária: ")
for lin in range(TAM):
    for col in range(TAM):
        if lin+col>TAM-1:
            print(f" {mat[lin][col]}")