#_______________EXERCICIO_16_________________________________
#Apresente a média de salário da população, a média de filhos e o maior salário.
qtd = 0
t_filhos = 0
t_salario = 0
maior = 0
salario = float(input("Informe o salario ou digite (-1) para finalizar:"))
while (salario != -1):
    if(salario > maior):
        maior = salario
    filhos = float(input("Informe o numero de filhos:"))
    qtd = qtd + 1
    t_filhos = t_filhos + filhos
    t_salario = t_salario + salario
    salario = float(input("Informe o salario ou digite (-1) para finalizar:"))
print(f"A média de salários é: {t_salario/qtd:.3f}");
print(f"A média de filhos é: {t_filhos/qtd:.2f}");
print(f"O maior salário é: {maior:.2f}");


# Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
 # int main(){
	# setlocale(LC_ALL, "Portuguese");
	# int filhos,qtd;
	# float salario,t_salario,t_filhos,maior;
	# qtd = 0;
	# t_filhos = 0 ;
	# t_salario = 0;
	# maior= 0;
	# printf("Informe o salario ou digite (-1) para finalizar:\n");
	# scanf("%f",&salario);
	# while (salario != -1)
	# {
	# 	if (salario > maior){
	# 		maior  = salario;
	# 	}
	# 		printf("Informe o numero de filhos:\n");
	# 		scanf("%d",&filhos);
	# 		qtd++;
	# 		t_filhos= t_filhos + filhos;
	# 		t_salario = t_salario + salario;
	# 		printf("Informe o salario ou digite (-1) para finalizar:\n");
	# 		scanf("%f",&salario);
	# 	}
	# printf("A média de salários é: %.3f\n",t_salario/qtd);
	# printf("A média de filhos é: %.2f\n",t_filhos/qtd);
	# printf("O maior salário é: %.3f\n",maior);
	# return(0);
	# }