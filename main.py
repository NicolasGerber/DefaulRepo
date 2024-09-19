#_______________EXERCICIO_14_________________________________
#Elabore um programa que apresente todos os números divisíveis por três que sejam menores que 100.
for i in range(3,100,3):
    print(f"{i}")


#Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#int main(){
# setlocale(LC_ALL, "Portuguese");
# int i;
# for (i=3;i<=100;i=i+3)
# {
# 	printf("Estes são os numeros divisiveis por 3:\n");
# 	system("pause");
# 	printf("%d\n",i);
# }
# return(0);
 # }
