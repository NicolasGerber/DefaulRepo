
# Solicita ao usuário para digitar as quatro notas
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n3 = float(input("Digite a terceira nota:"))
n4 = float(input("Digite a quarta nota:"))

# Caucula a média artimetica delas
media = (n1+n2+n3+n4)/4

# Exibe o resultado
print(f"A média é: {media}")

# Codigo em C
#include <stdio.h>
#int main()
#{
#float nota1,nota2,nota3,nota4,media;
#    printf("Escreva a primeira nota:");
#    scanf("%f",&nota1);
#    printf("Escreva a segunda nota:");
#    scanf("%f",&nota2);
#    printf("Escreva a terceira nota:");
#    scanf("%f",&nota3);
#    printf("Escreva a quarta nota:");
#    scanf("%f",&nota4);
#    media = (nota1 + nota2 + nota3 + nota4)/4;
#    printf("A media e: %.2f",media);
#    return (0);
#}