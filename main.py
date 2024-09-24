#_______________EXERCICIO_21________________________________
#faça um programa que apresenta a soma de todos os números inteiros ímpares entre 200 e 500.

soma = 0
for i in range (200,500,1):
    if (i % 2 != 0) :
        soma = soma + i
print(f"A soma dos impares de 200 ate 500 é: {soma}")

# Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#  int main(){
# 	setlocale(LC_ALL, "Portuguese");
# 	int i,soma;
# 	soma = 0;
# 	for (i=200;i<=500;i++){
# 		if (i % 2 != 0){
# 			soma = soma + i;
# 		}
# 	}
# 	printf("A soma dos impares de 200 até 500 é: %d",soma);
# 	return(0);
# }