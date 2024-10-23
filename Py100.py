import random

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
simbolos = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numeros = ['1','2','3','4','5','6','7','8','9','0']
v_senha = []

print("GERADOR AUTOMATICO DE SENHA")
n_letras = int(input("Quantas letras deve conter em sua senha?\nResposta:"))
n_simbolos = int(input("Quantos simbolos deve conter em sua senha?:\nResposta:"))
n_numeros =  int(input("Quantos simbolos deve conter em sua senha?:\nResposta:"))


for i in range(0,n_letras):
    v_senha.append(random.choice(letras))
for i in range(0,n_simbolos):
    v_senha.append(random.choice(simbolos))
for i in range(0,n_numeros):
    v_senha.append(random.choice(numeros))
random.shuffle(v_senha)
senha=""
for i in v_senha:
    senha+=i
print(f"SUA SENHA É: {senha}")