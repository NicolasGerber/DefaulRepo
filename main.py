#_______________EXERCICIO_23________________________________
#Elabore um programa que leia uma frase e o número de vezes que deseja imprimi-la.
frase = (input("Escreva uma frase:"))
qtd = int(input("Quantas vezes essa frase deve ser repetida:"))

for i in range (qtd):
    print(frase)


#Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#  int main(){
# 	setlocale(LC_ALL, "Portuguese");
# 	int i,qtd;
# 	char frase[100];
# 	printf ("Escreva Uma frase:");
# 	gets(frase);
# 	printf("Qunatas vezes essa frase deve ser repetida:");
# 	scanf("%d",&qtd);
# 	for (i=1;i<=qtd;i++){
# 		printf("%s\n",frase);
# 	}
# 	return(0);
# }