class Pokemon:
    from time import time
    vida_atual = 100
    def __init__(self,jogador,pokemon_inicial):
        self.jogador = jogador
        self.pokemon_inicial = pokemon_inicial
        self.vida = 100

    def ataques(self,ataque):
        p1 = "Lança Chamas"
        p2 = "Explosão de Fogo"
        p3 = "Tela de Fumaça"
        p4 = "Brasas"
        if ataque == 1:

            print(f"{self.pokemon_inicial} use o {p1}")
            self.dano = 20
        elif ataque == 2:

            print(f"{self.pokemon_inicial} use o {p2}")
            self.dano = 25
        elif ataque == 3:
            print(f"{self.pokemon_inicial} use o {p3}")
            self.dano = 0
        elif ataque == 4:

            print(f"{self.pokemon_inicial} use o {p4}")
            self.dano = 5

