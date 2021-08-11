class Pokemon_Back2:

    vida_atual = 100
    vida = 100
    dano = 0
    def __init__(self,jogador2,pokemon2):
        self.jogador2 = jogador2
        self.pokemon2 = pokemon2
        self.global_var = 0
    def ataques(self,ataque):
        p1 = "Choque do Trovão"
        p2 = "Cauda de Ferro"
        p3 = "Investida Trovão"
        p4 = "Charme"
        if ataque == 1:
            print(f"{self.pokemon2} use o {p1}")
            self.dano = 15

        elif ataque == 2:
            print(f"{self.pokemon2} use o {p2}")
            self.dano = 20
        elif ataque == 3:
            print(f"{self.pokemon2} use o {p3}")
            self.dano = 21
        elif ataque == 4:
            print(f"{self.pokemon2} use o {p4}")
            self.dano = 0

