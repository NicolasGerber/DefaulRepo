# Solicita ao usuário para digitar um número
num = int(input("Digite um número: "))

# Calcula o próximo e o número anterior
prox = num + 1
ant = num - 1

# Exibe os resultados
print(f"Você digitou: {num}")
print(f"O próximo número é: {prox}")
print(f"O número anterior é: {ant}")

#Versão C
# #include <stdio.h>
#int main()
#{
#int num, prox, ant;
#      printf("Digite um numero:");
#      scanf("%d", &num);
#      prox = num + 1;
#      ant = num - 1;
#     printf("Voce digitou: %d\n",num);
#     printf("O proximo numero e: %d\n",prox);
#    printf("O numero anterior e: %d\n", ant);
#   return (0);
#     }