#_______________EXERCICIO_24________________________________
#Faça um programa que leia um conjunto de pedidos e calcule o total da compra. O
# pedido possui os seguintes campos: número, data (dia, mês e ano), preço unitário
# e quantidade. A entrada de pedidos é encerrada quando o usuário informa zero
# como número do pedido.

preco_t = 0
total_pedido = 0
pedido = int(input("Digite o numero do pedido:"))
while (pedido != 0):
    total_pedido = total_pedido + 1
    data = (input("Informe a data do pedido:"))
    preco_q = 0
    preco_u = float(input("Informe preço unitario do produto:"))
    qtd = int(input("Informe a quantidade:"))
    preco_q = preco_u * qtd
    preco_t = preco_t + preco_u
    pedido = int(input("Digite o numero do pedido:"))
print(f"O total de pedidos foi {total_pedido}, totalizando no total R$ {preco_t:.2f} ate a data de {data}");

# Versão em C
# include <stdio.h>
# include <stdlib.h>
# include <locale.h>
# include <string.h>
# int
# main()
# {
#     setlocale(LC_ALL, "Portuguese");
# int
# pedido, qtd, total_pedidos;
# float
# preco_u, preco_q, preco_t;
# char
# data[9];
# preco_t = 0;
# printf("Digite o numero do pedido:\n");
# scanf("%d", & pedido);
# while (pedido != 0){
# total_pedidos++;
# printf("Informe a data do pedido:\n");
# scanf("%s", & data);
# preco_q = 0;
# printf("Informe preço unitario do produto:\n");
# scanf("%f", & preco_u);
# printf("Informe a quantidade:\n");
# scanf("%d", & qtd);
# preco_q = preco_u * qtd;
# preco_t = preco_t + preco_u;
# printf("Digite o numero do pedido:\n");
# scanf("%d", & pedido);
# }
# printf("O total de pedidos foi %d, totalizando no total R$ %.2f ate a data de %s", total_pedidos, preco_t, data);
# return (0);
# }
