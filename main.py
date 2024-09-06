#_______________EXERCICIO_5___________________________________
#Elabore um programa que calcule a área de um trapézio.

B= float(input("Informe a Base Inferior do trapezio:"))
b= float(input("Informe a Base Superior do Trapezio:"))
h= float(input("Informe a Altura do Trapezio:"))
area = ((B+b)*h)/ 2
print(f"A area do trapézio é:{area}")

# VERSÃO EM C
# include <stdio.h>
# include <math.h>
# int main()
# {
#    float B, b, h, area;
#    printf("Informe a Base Inferior do trapezio:");
#    scanf("%f", &B);
#    printf("Informe a Base Superior do Trapezio:");
#    scanf("%f", &b);
#    printf("Informe a Altura do Trapezio:");
#    scanf("%f", &h);
#    area = ((B + b) * h) / 2;
#    printf("\nA area do trapezio e: %.2f", area);
#    return(0);
# }