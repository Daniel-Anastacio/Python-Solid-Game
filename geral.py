class Competidores:
    placar = []


class Usuario(Competidores):
    def __init__(self):
        super().__init__()
        self.nome = self.pergunta("Digite seu nome")
        self.vidas = 5
        self.pontos = 0

    def registrar(self):
        Competidores.placar.append({self.nome: self.pontos})
        print(Competidores.placar)

    def resultados(self):
        print(f"{self.nome}, você tem {self.vidas} vidas e {self.pontos} pontos ")

    def pergunta(self, pergunta):
        try:
            return str(input(pergunta))
        except:
            print("Digite um nome válido")
            self.pergunta(pergunta)


def apresentações():
    print("Bem Vindo ao jogo da forca\nRegras\nEstes são os recordes:\n")


def inicializar():
    player = Usuario()
    player.registrar()


# def player():
#     try:
#         return str(input("Digite seu nome\n"))
#     except:
#         print("Digite um nome válido")
#         player()
