#importando biblioteca randômica
import random
#definir o tamanho da matriz
TAM = 3
#Definido um laço para a matriz que 
# intera TAM vezes
mat1 = [[] for _ in range(TAM)]
mat2 = [[] for _ in range(TAM)]
mat3 = [[0 for _ in range(TAM)] for _ in range(TAM)]

#Função soma
def soma():
    for lin in range(TAM):
        for col in range(TAM):
            mat3[lin][col] = mat1[lin][col] + mat2[lin][col]

#Função subtração
def sub():
    for lin in range(TAM):
        for col in range(TAM):
            mat3[lin][col] = mat1[lin][col] - mat2[lin][col]

#Função multiplicacao
def mult():
    for lin in range(TAM):
        for col in range(TAM):
            mat3[lin][col] = mat1[lin][col] * mat2[lin][col]

#Função divisão
def div():
    for lin in range(TAM):
        for col in range(TAM):
            if mat1[lin][col] != 0 and mat2[lin][col] != 0:
                mat3[lin][col] = mat1[lin][col] / mat2[lin][col]
            elif ZeroDivisionError:
                print('')

#preenchendo a matriz com nros aleatórios
for lin in range(TAM):
    for col in range(TAM):
        mat1[lin].append(random.randrange(0,10))
        mat2[lin].append(random.randrange(0,10))



#para exibir
print("Matriz 1:")
for cont in mat1:
    print(cont)

print("Matriz 2")
for cont in mat2:
    print(cont)

print ("Matriz Soma")
soma()
for cont in mat3:
    print(cont)

print ("Matriz Subtração")
sub()
for cont in mat3:
    print(cont)

print ("Matriz Multiplicação")
mult()
for cont in mat3:
    print(cont)

print ("Matriz Divisão")
div()
for cont in mat3:
    print(cont)