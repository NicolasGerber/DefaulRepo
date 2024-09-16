#_______________EXERCICIO_10_________________________________
#Escreva um algoritimo que receba o nome idade do usuario , assim informando o valor da mensalidade baseado na sua idade
nome = input("Informe seu nome completo:")
idade=int(input("Informe sua idade:"))
if idade > 65:
    valor = 170
elif idade >= 46:
    valor = 130
elif idade >= 30:
    valor = 90
elif idade >= 19:
    valor = 70
else:
    valor = 50
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Mensalidade: {valor:.2f}")

#Versão em C
# include <stdio.h>
# include <stdlib.h>
# include <locale.h>
# include <string.h>
# int
# main()
# {
#     setlocale(LC_ALL, "Portuguese");
# int
# idade;
# char
# nome[50];
# float
# valor;
# printf("Informe seu nome:");
# fgets(nome, sizeof(nome), stdin);
# size_t
# len = strlen(nome);
# if (len > 0 & & nome[len - 1] == '\n')
# {
#     nome[len - 1] = '\0';
# }
#
# printf("Informe sua idade:");
# scanf("%d", & idade);
# valor = 0;
# if (idade > 65)
# {
#     valor = 170;
# } else if (idade >= 46 & & idade <= 65) {
# valor = 130;
# } else if (idade >= 30 & & idade <= 45) {
# valor = 90;
# } else if (idade >= 19 & & idade <= 29) {
# valor = 70;
# } else {
# valor = 50;
# }
# printf("Nome: %s\nIdade: %d\nMensalidade: %.2f\n", nome, idade, valor);
#
# return (0);
# }