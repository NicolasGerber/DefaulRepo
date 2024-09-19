#_______________EXERCICIO_15_________________________________
#Construa um programa que receba um número inteiro maior que um e verifique se ele é primo.
num=int(input("Escreva um numero inteiro maior que 1:"))
qtd=0
for i in range(1,num +1):
     if (num % i == 0):
         qtd +=1
if qtd==2:
     print(f"0 numero é primo")
else:
     print(f"O numero não é primo")


# versão em C
# include <stdio.h>
# include <stdlib.h>
# include <locale.h>
# include <string.h>
# int
# main()
# {
#     setlocale(LC_ALL, "Portuguese");
# int
# num, i, qtd;
# printf("Digite um numero inteiro maior que 1:\n");
# scanf("%d", & num);
# qtd = 0;
# for (i=1;i <= num;i++)
# {
# if (num % i == 0)
# qtd + +;
# }
# if (qtd == 2)
# printf("O numero é primo. \n");
# else
# printf("Não é primo\n");
# return (0);
# }

