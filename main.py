#_______________EXERCICIO_29________________________________
# elabore uma função que receba dois números positivos por parâmetro e
# retorne a soma dos N números inteiros existentes entre eles.
def soma(n1,n2):
    if n1 > n2:
        troca = n1
        n1 = n2
        n2 = troca
    soma = 0
    for i in range(n1 + 1, n2):
        soma += i
    return soma
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
resultado = soma(num1,num2)
print(f"A soma dos inteiros entre {num1} e {num2} é {resultado}")



#VERSÃO EM C
# int soma(int n1, int n2){
# 	int i,troca,soma;
# 	if (n1 > n2){
# 		troca = n1;
# 		n1 = n2;
# 		n2 = troca;
# 	}
# 	for (i=n1+1;i<n2;i++){
# 		soma = soma + i;
# 	}
# 	return(soma);
# }
#
# int main() {
#     setlocale(LC_ALL, "Portuguese");
# 	int num1, num2, total;
# 	printf("Digite o primeiro numero:\n");
# 	scanf("%d",&num1);
# 	printf("Digite o segundo numero:\n");
# 	scanf("%d",&num2);
# 	total = soma(num1,num2);
# 	printf("A soma dos inteiro entre %d e %d é: %d",num1,num2,total);
# }

