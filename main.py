#_______________EXERCICIO_12_________________________________
#Faça um programa que leia um número inteiro e calcule o seu fatorial.
num=int(input("Escreva um numero inteiro positivo:"))
fat = 1
for i in range(1,num + 1):
        fat *= i
        if i == num:
           break
print(f"O fatorial de {num} é: {fat}")

# Versão em C
# include <stdio.h>
# include <stdlib.h>
# include <locale.h>
# include <string.h>
# int
# main()
# {
#         setlocale(LC_ALL, "Portuguese");
# int
# num, i, fat;
# printf("Digite um numero inteiro positivo:");
# scanf("%d", & num);
# fat = 1;
# for (i=1;i <= num;i++)
# {
#
#         fat = fat * i;
#
# }
# printf("O fatorial de %d é :%d", num, fat);
# return (0);
# }