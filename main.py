#_______________EXERCICIO_9_________________________________
#Escreva um algoritimo que leia 4 notas de um aluno e entregue (Reprovado,Aprovado ou Exame)
n1 = float(input("Escreva a primeira nota: "))
n2 = float(input("Escreva a segunda nota: "))
n3 = float(input("Escreva a terceira nota: "))
n4 = float(input("Escreva a quarta nota: "))
total = n1+n2+n3+n4
media = total/4
if media >= 7:
    print(f"Media final: {media:.2f} \nStatus: Aprovado")
elif media < 4:
    print(f"Media final: {media:.2f} \nStatus: Reprovado")
else:
    print(f"Media final: {media:.2f} \nStatus: Exame")


#Versão em C
# include <stdio.h>
# int
# main()
# {
#
#     float n1, n2, n3, n4, media, total;
# printf("Escreva a primeira nota:");
# scanf("%f", & n1);
# printf("Escreva a segunda nota:");
# scanf("%f", & n2);
# printf("Escreva a terceira nota:");
# scanf("%f", & n3);
# printf("Escreva a quarta nota:");
# scanf("%f", & n4);
# total = n1 + n2 + n3 + n4;
# media = total / 4;
# if (media >= 7)
# {
#     printf("Media final:%.2f \nStatus:Aprovado", media);
# } else {
# if (media < 4)
# {
#     printf("Media final:%.2f \nStatus:Reprovado", media);
# } else {
#     printf("Media final:%.2f \nStatus:Exame", media);
# }
# }
# return (0);
# }
#
