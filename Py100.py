import random
from LISTA import word_list
palavra_escolhida = random.choice(word_list)


tamanho = len(palavra_escolhida)
placeholder = ""
for posição in range(tamanho):
    placeholder += "_"
print(placeholder)

tentativas = 6
game_over = False
letras_certas= []

print("FORCA")
while not game_over:

    chute = input("Adivinhe uma letra: ").lower()

    display = ""
    if chute in letras_certas:
        print("VOCÊ JA ACERTOU ESSA LETRA!")

    for letra in palavra_escolhida:
        if letra == chute:
            display += letra
            letras_certas.append(chute)

        elif letra in letras_certas:
            display += letra
        else:
            display += "_"

    print(display)
    if chute not in palavra_escolhida:
        tentativas -= 1
        print(f"LETRA ERRADA! \nVIDAS RESTANTES: {tentativas}\n")

        if tentativas == 0:
            game_over = True
            print("**********VOCÊ**PERDEU*********")
            print(f"A palavra era: {palavra_escolhida.upper()}")

    if "_" not in display:
        print("**********VOCÊ**GANHOU!**********")
        game_over = True


