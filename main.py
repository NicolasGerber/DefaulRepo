#_______________EXERCICIO_18________________________________
#Faça um programa que leia idade e opinião e apresente:
#O número de clientes que responderam satisfatório, a média de idade dos clientes que opinaram como satisfatório.
#E o número de clientes que responderam insatisfatório.
# O programa se encerra quando for digitado o valor zero para idade.
qtd=0
t_idade = 0
m_idade = 0
cont = 0
sat = 0
insat = 0

idade = int(input("Digite a idade do cliente ou (0) para finalizar:"))
while (idade != 0):
    print(f"Como foi sua experiencia com o produto?\n")
    opn = int(input("1 – satisfatório \n2 – indiferente \n3 – insatisfatório\n"))
    qtd = qtd + 1
    t_idade = t_idade + idade
    if (opn == 1):
        sat = sat +1
    elif (opn == 3):
        insat = insat + 1
    idade = int(input("Digite a idade do cliente ou (0) para finalizar:"))
m_idade = t_idade/qtd
print(f"A Quantidade de cliente que responderam como satisfatorio foi: {sat}")
print(f"A media de idade deles é: {m_idade:.2f}")
print(f"A Quantidade de cliente que responderam como insatisfatorio foi: {insat}")



# Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#  int main(){
# 	setlocale(LC_ALL, "Portuguese");
# 	int qtd,idade,opn,cont,t_idade,insat,sat;
# 	float m_idade;
# 	qtd=0;
# 	t_idade = 0;
# 	m_idade = 0;
# 	cont = 0;
# 	sat = 0;
# 	insat = 0;
# 	printf("Digite a idade do cliente ou (0) para finalizar:\n");
# 	scanf("%d",&idade);
# 	while (idade !=0){
# 		printf("Como foi sua experiencia com o produto?\n");
# 		printf("1 – satisfatório \n2 – indiferente \n3 – insatisfatório\n");
# 		scanf("%d",&opn);
# 		qtd++;
# 		t_idade = t_idade + idade;
# 		if (opn == 1){
# 			sat++;
# 		} else if (opn == 3){
# 			insat++;
# 		}
# 		printf("Digite a idade do cliente ou (0) para finalizar:\n");
# 		scanf("%d",&idade);
# 	}
# 	m_idade = t_idade/qtd;
# 	printf("A Quantidade de cliente que responderam como satisfatorio foi: %d\n",sat);
# 	printf("A media de idade deles é: %.2f\n",m_idade);
# 	printf("A Quantidade de cliente que responderam como insatisfatorio foi: %d\n",insat);
# 	return(0);
# }