#_______________EXERCICIO_8__________________________________
#Escreva um programa que peça dois numeros ao usuario, informe o maior e menor, e informe caso sejam iguais
n1 = int(input("Escreva o primeiro numero:"))
n2 = int(input("Escreva o segundo numero:"))
if n1 != n2:
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    print(f"O maior numero é {maior} e o menor numero é {menor}")
else:
    print(f"Os numeros são iguais")