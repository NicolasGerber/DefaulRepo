#_______________EXERCICIO_3___________________________________
#Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e
#apresente o valor do rendimento e o valor total (valor do depósito + valor do rendimento).

depositado = float(input("Digite o valor depositado:"))
txjuro = float(input("Indique a taxa de juro:"))
rendimento = depositado * (txjuro/100)
vtotal = depositado + rendimento

print(f"O valor do rendimento é: {rendimento:.2f}")
print(f"O valor total da aplicação sera de:{vtotal:.2f}")

#   VERSÃO EM C
#include <stdio.h>
#int main()
#{
#    float depositado, txjuro, rendimento, vtotal;
#    printf("Escreva o valor depositado:");
#    scanf("%f", &depositado);
#    printf("Indique a taxa de juros:");
#    scanf("%f", &txjuro);
#    rendimento = depositado * (txjuro / 100);
#    vtotal = depositado + rendimento;
#    printf("O valor de rendimento sera de %.2f:\n", rendimento);
#    system("pause");
#    printf("O valor total sera de %.2f:", vtotal);
#    return (0);
#}

