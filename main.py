#_______________EXERCICIO_4___________________________________
#Escreva um programa que receba dois números, calcule e apresente o resultado
#do primeiro número elevado ao segundo.
n1=int(input("Escreva o numera a ser elevado:"))
n2=int(input("Escreva a potencia a que {} sera elevado:".format(n1))) #usei o .format para mostrar na box o primeiro numero digitado

print("O resultado da potencia sera:",(n1**n2))
#   VERSÃO EM C
#include <stdio.h>
#include <math.h>
#int main()
#{
#    int n1, n2, potencia;
#
#    printf("Escreva o numero a ser elevado:");
#    scanf("%d", &n1);
#    printf("Escreva a potencia a que %d sera elevado:", n1);
#    scanf("%d", &n2);
#    potencia = pow(n1, n2);
#    printf("\nO resultado da potencia sera %d:", potencia);
#    return(0);
#}