import random
from LISTA import jogadores

def pick():
    jogador = random.choice(jogadores)
    goals = jogador['gols']
    return f"{jogador['nome']}, conhecido por sua atuação no {jogador['time']}", goals

def game():
    score = 0
    errou = False

    while not errou:
        print("Bem-vindo ao HIGHER/LOWER!:\nVocê terá de adivinhar se um jogador tem mais ou menos gols que outro na carreira!\n")

        jogador_a, gols_a = pick()
        jogador_b, gols_b = pick()

        print(f"Jogador A: {jogador_a} com {gols_a} gols.")
        print(f"Jogador B: {jogador_b} com {gols_b} gols.")

        escolha = input("Quem tem mais gols? A ou B: ").strip().upper()

        if (escolha == 'A' and gols_a > gols_b) or (escolha == 'B' and gols_b > gols_a):
            print("Você acertou!")
            score += 1
            print("\n"*10)
            print(f"Score atual: {score}\n")
        else:
            print("Você errou!")
            print(f"Score final: {score}")
            errou = True

game()
