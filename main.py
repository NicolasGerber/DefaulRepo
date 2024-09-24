#_______________EXERCICIO_22________________________________
#Construa um programa que apresente todos os números divisíveis por três e por sete que sejam menores que 30.

#NOTA
# No gabarito oficial da questão era visto que seriam entregues todos os numeros divisiveis por 3 e 7 menores que 30
# mas na minha interpretação da questão seriam somente os numeros que seria divisiveis por 3 E 7.

for i in range(1,30,1):
    if (i % 3 == 0):
        print(f"O numero {i} é divisivel por 3")
    elif (i % 7 == 0):
        print(f"O numero {i} é divisivel por 7")

# Na minha interpretação deveria ser realizado uma verificação conjunta pela clausula AND
for i in range(1,30,1):
    if (i % 3 == 0 and i % 7 == 0):
        print(f"O numero {i} é divisivel por 3 e 7")


#Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#  int main(){
# 	setlocale(LC_ALL, "Portuguese");
# 	int i;
# 	for (i=1;i<=30;i++){
# 		if (i % 3 == 0){
# 			printf("O numero %d é divisel por 3\n",i);
# 		}
# 		if (i % 7 == 0){
# 			printf("O numero %d é divisel por 7\n",i);
# 		}
# 	}
# 	return(0);
# }