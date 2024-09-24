#_______________EXERCICIO_20________________________________
#Imagine que você esteja ensinando a tabuada para uma criança e precisa mostrar
# a ela todas as possíveis multiplicações entre os números que vão de um até dez.
# Assim, elabore um programa que imprima a tabuada do um ao dez.
for i in range(1,10,1):
    print(f"Tabuada do {i}")
    for j in range (1,10,1):
        valor = i*j
        print(f"{i} x {j} = {valor}")

#Versão C
# include <stdio.h>
# include <stdlib.h>
# include <locale.h>
# include <string.h>
# int
# main()
# {
#     setlocale(LC_ALL, "Portuguese");
# int
# valor, j, i;
# for (i=1;i <= 10;i++)
# {
#     printf("tabuada do %d\n", i);
# system("pause");
# for (j=1;j <= 10;j++)
# {
#     valor = i * j;
# printf("%d x %d = %d\n", i, j, valor);
# }
#
# }
# return (0);
# }