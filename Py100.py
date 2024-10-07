conta=float(input("Qual foi total da conta?:"))
tip=float(input("Quanto voce gostaria dar de gorjeta? (10%,12% ou 15%):"))
div=int(input("Quantas pessoas vão dividir a conta:"))

porcento = tip/100
gorjeta = conta*porcento
total= (conta + gorjeta)/div
round(total,2)
print(f"Cada pessoa deve pagar {total}")