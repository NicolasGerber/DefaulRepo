#_______________EXERCICIO_17_________________________________
#calcule e apresente a média de altura e idade das pessoas. A entrada de dados é encerrada quando for digitado o valor zero para a idade.
t_idade = 0
t_alt = 0
m_idade = 0
m_alt = 0
qtd=0
idade = int(input("Digite a idade ou (0) para finalizar:"))
while (idade != 0):
    alt=float(input("Digite sua altura"))
    qtd = qtd + 1
    t_alt = t_alt + alt
    t_idade = t_idade + idade
    idade = int(input("Digite a idade ou (0) para finalizar:"))
m_idade = t_idade/qtd
m_alt = t_alt/qtd
print(f"A media de idade é: {m_idade:.2f}")
print(f"A media de altura é: {m_alt:.2f}")


# Versão em C
# include <stdio.h>
# include <stdlib.h>
# include <locale.h>
# include <string.h>
# int
# main()
# {
#     setlocale(LC_ALL, "Portuguese");
# int
# idade, qtd;
# float
# alt, m_idade, m_alt, t_alt, t_idade;
# t_idade = 0;
# t_alt = 0;
# m_idade = 0;
# m_alt = 0;
# qtd = 0;
# printf("Digite a idade ou (0) para finalizar:\n");
# scanf("%d", & idade);
# while (idade != 0){
# printf("Digite sua altura:");
# scanf("%f", & alt);
# qtd++;
# t_alt = t_alt + alt;
# t_idade = t_idade + idade;
# printf("Digite a idade ou (0) para finalizar:\n");
# scanf("%d", & idade);
# }
# m_idade = t_idade / qtd;
# m_alt = t_alt / qtd;
# printf("A media de idade é: %.2f \n", m_idade);
# printf("A media de altura é: %.2f \n", m_alt);
# return (0);
# }
