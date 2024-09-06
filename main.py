#_______________EXERCICIO_6__________________________________
#Escreva um programa que leia um número positivo inteiro e apresente o quadrado e a raiz quadrada deste número.
import math #importar a biblioteca math
num = int(input("Escreva um numero positivo inteiro:"))
quadrado = (num ** 2)
raiz = math.sqrt(num)

print(f"O numero {num} ao quadrado é: {quadrado}")
print(f"A raiz quadrada de {num} é: {raiz}")

# VERSÃO C
# include <stdio.h>
# include <math.h>
# int
# main()
# {
#     int
# num, quadrado;
# float
# raiz;
# printf("Escreva um numero inteiro positivo:");
# scanf("%d", & num);
# quadrado = pow(num, 2);
# raiz = sqrt(num);
# printf("\nO numero %d ao quadrado e: %d", num, quadrado);
# printf("\nA raiz quadrada de %d e %.2f:", num, raiz);
#
# return (0);
# }