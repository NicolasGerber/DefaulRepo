#_______________EXERCICIO_26________________________________
#Elaborer um vetor que armazene os numeros e os ordene.
vetorA = []
for i in range(10):
    elemento =int(input(f"Digite o {i+1}ª elemento do vetor:"))
    vetorA.append(elemento)

    for i in range (len(vetorA) - 1):
        for j in range(i+1, len(vetorA)):
            if vetorA[i] > vetorA[j]:
                vetorA[i], vetorA[j] = vetorA[j], vetorA[i]
    print("\nVETOR ORDENADO:")
    for elemento in vetorA:
            print(f"{elemento} - ", end="")
    print()

    # Versão em C
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#  int main(){
# 	setlocale(LC_ALL, "Portuguese");
# 	int vetorA[10];
# 	int i,j,troca;
# 	for (i=0;i<10;i++){
# 		printf("Digite o %d elemento do vetor:\n",i);
# 		scanf("%d",&vetorA[i]);
# 		}
# 	for (i=0;i<9;i++){
# 		for (j=i+1;j<10;j++){
# 			if(vetorA[i] > vetorA[j]){
# 				troca = vetorA[i];
# 				vetorA[i] = vetorA[j];
# 				vetorA[j] = troca;
# 			}
# 		}
# 	}
# 	printf("\n VETOR ORDENADO:\n");
# 	for (i=0;i<10;i++)
# 	{
# 		printf("%d - ", vetorA[i]);
# 	}
# 	return(0);
# }