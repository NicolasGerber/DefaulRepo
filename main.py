#_______________EXERCICIO_28.2________________________________
def converte(quilo):
    resultado = quilo * 2.2
    return resultado

peso = float(input("Digite o peso em quilos:\n"))
convertido = converte(peso)
print(f"{peso:.2f} quilos em libras é: {convertido:.2f}")

