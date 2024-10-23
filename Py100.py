import random
maquina = random.randint(1, 3)

escolha = int(input("JOKENPO!\n escolha\n 1-PEDRA\n 2-PAPEL\n 3-TESOURA\n"))
if escolha == 1 and maquina == 1:
    print("Você escolheu PEDRA")
    print("A Maquina escolheu PEDRA")
    print("EMPATE!")
elif escolha == 1 and maquina == 2:
    print("Você escolheu PEDRA")
    print("A Maquina escolheu PAPEL")
    print("PERDEU!")
elif escolha == 1 and maquina == 3:
    print("Você escolheu PEDRA")
    print("A Maquina escolheu TESOURA")
    print("GANHOU!")
if escolha == 2 and maquina == 1:
    print("Você escolheu PEPEL")
    print("A Maquina escolheu PEDRA")
    print("GANHOU!")
elif escolha == 2 and maquina == 2:
    print("Você escolheu PAPEL")
    print("A Maquina escolheu PAPEL")
    print("EMPATE!")
elif escolha == 2 and maquina == 3:
    print("Você escolheu PAPEL")
    print("A Maquina escolheu TESOURA")
    print("PERDEU!")
if escolha == 3 and maquina == 1:
    print("Você escolheu TESOURA")
    print("A Maquina escolheu PEDRA")
    print("PERDEU!")
elif escolha == 3 and maquina == 2:
    print("Você escolheu TESOURA")
    print("A Maquina escolheu PAPEL")
    print("GANHOU!")
elif escolha == 3 and maquina == 3:
    print("Você escolheu TESOURA")
    print("A Maquina escolheu TESOURA")
    print("EMPATE!")
