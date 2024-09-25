#_______________EXERCICIO_26________________________________
# Construa um programa que possibilite calcular a área total de uma residência (sala,
# cozinha, banheiro, quartos etc.). O programa deve solicitar a entrada do nome, a
# largura e o comprimento de determinado cômodo até que o nome do cômodo seja
# “FIM”. O programa deve apresentar o valor total acumulado da área residencial.
area = 0
total = 0
nome = (input("Escreva o nome do comodo ou (FIM) para finalizar:"))
while (nome.lower() != "fim"):
    largura = float(input("Escreva a largura do comodo:"))
    comprimento = float(input("Escreva o comprimento do comodo:"))
    area = largura * comprimento
    total += area
    nome = (input("Escreva o nome do comodo ou (FIM) para finalizar:"))
print(f"A area total da case é: {total:.2f}")

# Versão em C
# include <stdio.h>
# include <stdlib.h>
# include <locale.h>
# include <string.h>
# int
# main()
# {
#     setlocale(LC_ALL, "Portuguese");
# float
# largura, comprimento, area, total;
# char
# nome[50];
# printf("Escreva o nome do comodo ou digite (FIM) para finalizar:");
# fgets(nome, sizeof(nome), stdin);
# nome[strcspn(nome, "\n")] = 0;
# area = 0;
# total = 0;
# while (strcmp(nome, "fim") != 0 & & strcmp(nome, "FIM") != 0) {
# printf("\nDigite a largura do comodo:");
# scanf("%f", & largura);
# printf("\nDigite o comprimento do comodo:");
# scanf("%f", & comprimento);
# area = largura * comprimento;
# total = total + area;
# printf("\nEscreva o nome do comodo ou digite (FIM) para finalizar:");
# getchar();
# fgets(nome, sizeof(nome), stdin);
# nome[strcspn(nome, "\n")] = 0;;
# }
# printf("\nA area total da casa é: %.2f", total);
# return (0);
# }
