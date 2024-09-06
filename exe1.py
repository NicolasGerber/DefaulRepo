#Escreva um programa que leia um número positivo inteiro e apresente o quadrado e a raiz quadrada deste número.
import math #importar a biblioteca math
num = int(input("Escreva um numero positivo inteiro:"))
quadrado = (num ** 2)
raiz = math.sqrt(num)

print(f"O numero {num} ao quadrado é: {quadrado}")
print(f"A raiz quadrada de {num} é: {raiz}")