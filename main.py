#_______________EXERCICIO_28________________________________
#Elaborer um vetor que armazene os numeros e os busque
#

vetorA = []
for i in range(10):
    elemento =int(input(f"Digite o {i+1}ª elemento do vetor:"))
    vetorA.append(elemento)

busca = int(input("Informe o elemento que deseja buscar:"))
posicoes = []

for i in range(len(vetorA)):
    if vetorA[i] == busca:
        posicoes.append(i+1)

if posicoes:
    print(f"O elemento {busca} foi encontrado nas posições: {', '.join(map(str, posicoes))}.")
else:
    print("O elemento não foi localizado.")


