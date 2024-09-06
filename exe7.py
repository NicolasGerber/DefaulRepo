#EXERCICIO 7
# Escreva um programa que, dado o raio de um círculo, calcule sua área e o perímetro.
import math
r = float(input("Escreva o raio do circulo:"))
A = math.pi*(r**2)
P = 2*(math.pi*r)
print(f"A area do circulo é: {A:.2f}")
print(f"O perimetro do circulo é: {P:.2f}")

#VERSAO EM C
# include <stdio.h>
# include <conio.h>
# include <math.h>
# define PI 3.14
# int
# main()
# {float
# r, A, P;
# printf("Escreva o raio do circulo:");
# scanf("%f", & r);
# A = PI * (pow(r, 2));
# P = 2 * (PI * r);
# printf("\nA area do circulo e: %.2f", A);
#
# printf("\nO perimetro do circulo e: %.2f", P);
#
# return (0);
# }