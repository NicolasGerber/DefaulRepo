#_______________EXERCICIO_18________________________________
#Faça um programa que leia números inteiros até que seja informado o valor 0.
# Apresente a média dos valores, o maior e o menor valor e a quantidade de números
# pares e ímpares

soma = 0
qtd = 0
impar = 0
par = 0
num=int(input("Escreva um numero ou digite (0) para finalizar:"))
maior = num
menor = num
while (num != 0):
    if (num > maior):
        maior = num
    elif (num < menor):
        menor = num
    qtd = qtd + 1
    soma = soma + num
    if (num % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

    num = int(input("Escreva um numero ou digite (0) para finalizar:"))
print(f"A media dos valores apresentados é :{soma/qtd:.2f}")
print(f"O maior numero apresentado foi : {maior}")
print(f"O menor numero apresentado foi: {menor}")
print(f"A quantidade de numeros pares é: {par}")
print(f"A quantidade de numeros impares é: {impar}")

#Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#  int main(){
# 	setlocale(LC_ALL, "Portuguese");
# 	int num,maior,menor,impar,par,soma,qtd,i;
# 	float media;
# 	printf("Informe um numero ou (0) para finalizar:\n");
# 	scanf("%d",&num);
# 	maior = num;
# 	menor = num;
# 	soma = 0;
# 	qtd = 0;
# 	impar = 0;
# 	par = 0;
# 	while (num != 0) {
# 		if (num > maior) {
# 			maior = num;
# 		} else if (num < menor){
# 			menor = num;
# 		}
# 		qtd ++;
# 		soma = soma + num;
# 		if (num % 2 == 0) {
# 			par++;
# 		} else {
# 			impar++;
# 		}
# 		printf("Informe um numero ou (0) para finalizar:\n");
# 		scanf("%d",&num);
# 	}
# 	media = soma/qtd;
# 	printf("A media dos valores apresentados é: %.2f\n", media);
# 	printf("O maior numero apresentado foi: %d\n", maior);
# 	printf("O menor numero apresentado foi: %d\n", menor);
# 	printf("A quantidade de numeros pares é: %d\n", par);
# 	printf("A quantidade de numeros impares é: %d", impar);
# 	return(0);
# }