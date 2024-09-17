#_______________EXERCICIO_11_________________________________
#Assim sendo, escreva um programa que receba cinco números inteiros e apresente o maior e o menor.
n1 = int(input("Escreva o primeiro numero:"))
maior = n1
menor = n1
n2 = int(input("Escreva o segundo numero:"))
if (n2 > maior):
    maior = n2
elif (n2 < menor):
    menor = n2
n3 = int(input("Escreva o terceiro numero:"))
if (n3 > maior):
    maior = n3
elif (n3 < menor):
    menor = n3
n4 = int(input("Escreva o quarto numero:"))
if (n4 > maior):
    maior = n4
elif (n4 < menor):
    menor = n4
n5 = int(input("Escreva o quinto numero:"))
if (n5 > maior):
    maior = n5
elif (n5 < menor):
    menor = n5
print(f"O maior numero é:{maior}")
print(f"O menor numero é:{menor}")



#Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
 # int main(){
	# setlocale(LC_ALL, "Portuguese");
	# int n1,n2,n3,n4,n5,maior,menor;
	# printf("Insira o primeiro numero:");
	# scanf("%d",&n1);
	# maior = n1;
	# menor = n1;
	# printf("Insira o segundo numero:");
	# scanf("%d",&n2);
	# if (n2 > n1) {
	# 	maior = n2;
	# } else if (n2 < n1) {
	# 	menor = n1;
	# }
	# printf("Insira o terceiro numero:");
	# scanf("%d",&n3);
	# if (n3 > maior) {
	# 	maior = n3;
	# } else if (n3 < menor) {
	# 	menor = n3;
	# }
	# printf("Insira o quarto numero:");
	# scanf("%d",&n4);
	# if (n4 > maior) {
	# 	maior = n4;
	# } else if (n4 < menor) {
	# 	menor = n4;
	# }
	# printf("Insira o quinto numero:");
	# scanf("%d",&n5);
	# if (n5 > maior) {
	# 	maior = n5;
	# } else if (n5 < menor) {
	# 	menor = n5;
	# }
	# printf("O maior numero é: %d",maior);
	# printf("\nO menor numero é: %d",menor);
 # 	return(0);
 # }