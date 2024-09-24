#_______________EXERCICIO_25________________________________
#Elabore um programa que receba a idade, o peso, o sexo e o estado civil de várias
# pessoas e imprima a quantidade daquelas que são casadas, solteiras, separadas
# e viúvas. Apresente a média de idade e de peso. O algoritmo finaliza quando for
# informado o valor zero para idade.
total_i = 0
media_i = 0
total_p = 0
media_p = 0
qtd = 0
casada = 0
solteira = 0
divorciada = 0
viuva = 0
idade = int(input("Digite a idade:"))
while (idade != 0):
    qtd = qtd + 1;
    total_i = total_i + idade
    peso = float(input("Digite o peso:"))
    total_p = total_p + peso
    sexo = (input("Digite o sexo:"))
    print("Digite o estado civil:")
    estado_cv = int(input("1 - Casado/a \n 2 - Solteiro/a \n 3 - Divorciado/a \n4 - Viuvo/a \n"))
    if (estado_cv == 1):
        casada = casada + 1
    elif (estado_cv == 2):
        solteira = solteira + 1
    elif (estado_cv == 3):
        divorciada = divorciada + 1
    elif (estado_cv == 4):
        viuva = viuva + 1
    idade = int(input("Digite a idade:"))
media_i = total_i/qtd
media_p = total_p/qtd
print(f"No total são:\n")
print(f"{casada} pessoas casadas\n")
print(f"{solteira} pessoas solteiras\n")
print(f"{divorciada} pessoas divorciadas\n")
print(f"{viuva} pessoas viuvas\n")
print(f"{media_i:.2f} média de idade é\n")
print(f"{media_p:.2f} média de peso é\n")


# Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
# int main(){
# 	setlocale(LC_ALL, "Portuguese");
# 	int qtd,idade,estado_cv,casada,solteira,divorciada,viuva;
# 	float peso,media_i,total_i,media_p,total_p;
# 	char sexo[1];
# 	total_i = 0;
# 	media_i = 0;
# 	total_p = 0;
# 	media_p = 0;
# 	printf("Digite a idade:\n");
# 	scanf("%d",&idade);
# 	while (idade != 0){
# 		qtd++;
# 		total_i = total_i + idade;
# 		printf("Digite o peso:\n");
# 		scanf("%f",&peso);
# 		total_p = total_p + peso;
# 		printf("Digite o sexo");
# 		scanf("%c",&sexo);
# 		printf("Digite o estado civil:\n");
# 		printf("1 - Casado/a \n 2 - Solteiro/a \n 3 - Divorciado/a \n 4 - Viuvo/a \n");
# 		scanf("%d", &estado_cv);
# 		switch (estado_cv){
# 			case 1: casada++;
# 			break;
# 			case 2: solteira++;
# 			break;
# 			case 3: divorciada++;
# 			break;
# 			case 4: viuva++;
# 			break;
# 		}
# 		printf("Digite a idade:\n");
# 		scanf("%d",&idade);
# 	}
# 	media_i = total_i/qtd;
# 	media_p = total_p/qtd;
# 	printf("No total são:\n");
# 	printf("%d pessoas casadas\n",casada);
# 	printf("%d pessoas solteiras\n",solteira);
# 	printf("%d pessoas divorciadas\n",divorciada);
# 	printf("%d pessoas viuvas\n",viuva);
# 	printf("A média de idade é:%.2f\n",media_i);
# 	printf("A média de peso é:%.2f\n",media_p);
# 	return(0);
# }