from pokemon_back import Pokemon
from pokemon_back2 import Pokemon_Back2
from time import sleep
from perder_vida import Perder_Vida
perder = Perder_Vida
p1 = Pokemon("Jogado1","Chamander")
p2 = Pokemon_Back2("Jogador2","Pikachu")
cont = 1
while True:
    if cont == 1:
        print(f"A Treinadora \033[34m{p1.jogador}\033[m escolhe seu pokemon \033[31m{p1.pokemon_inicial}\033[m")
        print()
        print(f"O Treinador \033[37m{p2.jogador2}\033[m escolhe seu pokemon \033[33m{p2.pokemon2}\033[m\n")

    ataque = int(input(f"\033[34m{p1.jogador}\033[m escolha o movimento\n"))

    p1.ataques(ataque)
    perder(p2.vida_atual, p1.dano,p2.pokemon2)
    p2.vida_atual -= p1.dano
    print()
    sleep(3)
    ataque2 = int(input(f"dIGITE O ATAQUE {p2.jogador2}\n".lower()))
    p2.ataques(ataque2)
    perder(p1.vida_atual, p2.dano,p1.pokemon_inicial)
    p1.vida_atual -= p2.dano

    cont += 1
