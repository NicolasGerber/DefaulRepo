#_______________EXERCICIO_28________________________________
def converte(celsius):
    resultado = (celsius * 1.8) + 32
    return resultado

temp = float(input("Digite a temperatura em Celsius:\n"))
convertido = converte(temp)
print(f"{temp:.2f} Graus Celsius em Fahrenheit é: {convertido:.2f}")

#VERSÃO EM C
# float converte(float celsius){
# 		float resultado;
# 		resultado = (celsius * 1.8) + 32;
# 		return(resultado);
# }
# int main() {
#     setlocale(LC_ALL, "Portuguese");
# 	system("cls");
# 	float temp,convertido;
# 	printf("Digite a temperatura em celcius:\n");
# 	scanf("%f",&temp);
# 	convertido = converte(temp);
# 	printf("%.2f Graus celcius em fahrenheit é: %.2f",temp,convertido);