class Perder_Vida:

    def __init__(self,vida_atual,dano,poke):

        self.vida_atual = vida_atual - dano
        self.vida_perdida = self.vida_atual
        if self.vida_atual >= 80:
            print(f"\033[35m{poke}\033[m perdeu \033[31m{dano}\033[m de pontos de vida ficando com \033[34m{self.vida_atual}hp\033[m ")
        elif self.vida_atual >=50 and self.vida_atual <= 79 :
            print(f"\033[35m{poke}\033[m perdeu \033[31m{dano}\033[m de pontos de vida ficando com \033[33m{self.vida_atual}hp\033[m ")
        elif self.vida_atual >= 1 and self.vida_atual <= 49:
            print(f"\033[35m{poke}\033[m perdeu \033[31m{dano}\033[m de pontos de vida ficando com \033[31m{self.vida_atual}hp\033[m ")
        else:
            self.vida_atual = 0
            print(
                f"\033[35m{poke}\033[m perdeu \033[31m{dano}\033[m de pontos de vida ficando com \033[31m{self.vida_atual}hp\033[m ")
            print("Game Over")

