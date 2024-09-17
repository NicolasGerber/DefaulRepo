#_______________EXERCICIO_12_________________________________
#Elabore um programa que receba o salário de um funcionário e o código do
# cargo e apresente o cargo, o valor do aumento e o novo salário.
print("Informe o cargo")
print("1- Servente")
print("2- Pedreiro")
print("3- Mestre de Obras")
print("4- Técnico de Segurança")
cargo = int(input("Digite o código referente ao cargo ocupado: "))
if cargo > 4:
    print("Código de cargo inválido.")
if cargo == 1:
        salario = float(input("Digite o salario do colaborador:"))
        reajuste = salario * 0.40
        salario_novo = salario + reajuste
        print(f"Para o cargo de Servente o reajuste foi de {reajuste:.2f} totalizando {salario_novo:.2f} de salário")
elif cargo == 2:
        salario = float(input("Digite o salario do colaborador:"))
        reajuste = salario * 0.35
        salario_novo = salario + reajuste
        print(f"Para o cargo de Pedreiro o reajuste foi de {reajuste:.2f} totalizando {salario_novo:.2f} de salário")
elif cargo == 3:
        salario = float(input("Digite o salario do colaborador:"))
        reajuste = salario * 0.20
        salario_novo = salario + reajuste
        print(f"Para o cargo de Mestre de Obras o reajuste foi de {reajuste:.2f} totalizando {salario_novo:.2f} de salário")
elif cargo == 4:
        salario = float(input("Digite o salario do colaborador:"))
        reajuste = salario * 0.10
        salario_novo = salario + reajuste
        print(f"Para o cargo de Técnico de Segurança o reajuste foi de {reajuste:.2f} totalizando {salario_novo:.2f} de salário")

#Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
 # int main(){
	# setlocale(LC_ALL, "Portuguese");
	# float salario,salario_novo;
	# int cargo;
	# printf("Informe o cargo:");
	# printf("\n1- Servente \n2- Pedreiro \n3- Mestre de Obras \n4- Técnico de Segurança \nDigite o codigo referente ao cargo ocupado:");
	# scanf("%d",&cargo);
	# printf("Informe o salario atual do colaborador:");
	# scanf("%f",&salario);
	# switch (cargo){
	# 	case 1:
	# 		salario_novo = salario + (salario*0.40);
	# 		printf("Para o cargo de Servente o reajuste foi de %.2f totalizando %.2f de salario",salario*0.40,salario_novo);
	# 		break;
	# 	case 2:
	# 		salario_novo = salario + (salario*0.35);
	# 		printf("Para o cargo de Pedreiro o reajuste foi de %.2f totalizando %.2f de salario",salario*0.35,salario_novo);
	# 		break;
	# 	case 3:
	# 		salario_novo = salario + (salario*0.20);
	# 		printf("Para o cargo de Mestre de Obras o reajuste foi de %.2f totalizando %.2f de salario",salario*0.20,salario_novo);
	# 		break;
	# 	case 4:
	# 		salario_novo = salario + (salario*0.10);
	# 		printf("Para o cargo de Técnico de Segurança o reajuste foi de %.2f totalizando %.2f de salario",salario*0.10,salario_novo);
	# 		break;
	# }
 # 	return(0);
 # }