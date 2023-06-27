import random

# ps = ["CAVALO", "CACHORRO", "HIENA", "FAISAO", 'ARARA', 'HIPOPÓTAMO', 'HIRAX', 'TARTIGRADO']
# ps = ps[random.randint(0, (len(ps) - 1))]
# vidas = 3
# pontuação = 0
# listchec = []
# listchec2 = []
#
# while vidas > 0 and pontuação < len(ps):
#     print('JOGO DA FORCA\nTEMA: ANIMAIS')
#     print(f'A palavra tem {len(ps)} letras')
#     letra = input('digite uma letra:\n')
#     letra = letra.upper()
#     if ps.count(letra) == 0:
#         vidas = vidas - 1
#         listchec2.append(letra)
#         print(
#             f"Esta letra não está na palavra secreta\nNúmero de vidas: {vidas}\nPontuação necessária para vencer: {len(ps)}\nPontuação atual: {pontuação}\nLetras Erradas: {str(listchec2)}\n")
#     else:
#         pontuação = pontuação + ps.count(letra)
#         print(
#             f'Essa letra aparece {ps.count(letra)} vez(es)\nnúmero de vidas: {vidas}\npontuação necessária para vencer: {len(ps)}\npontuação atual: {pontuação}\nLetras Erradas: {listchec2}\n')
#         for x in range(0, (len(ps))):
#             if letra == ps[x]:
#                 print(ps[x])
#                 listchec.append(ps[x])
#             elif letra != ps[x] and ps[x] in listchec:
#                 print(ps[x])
#             else:
#                 print('----')
# if pontuação == len(ps):
#     print(f"Parabéns você venceu a palavra correta é {ps}")
# elif vidas == 0:
#     print('Sua vidas chegaram a zero você perdeu')

######


Temas = ["Profissões", "Animais", "Lugares", "Nomes de Pessoa"]


class Usuario:
    def __init__(self):
        self.nome = self.pergunta("Digite seu nome")
        self.vidas = 5
        self.pontos = 0
        self.letra = None

    def registrar(self):
        Game.placar.append({self.nome: self.pontos})
        print(Game.placar)

    def resultados(self):
        print(f"{self.nome}, você tem {self.vidas} vidas e {self.pontos} pontos ")

    def pergunta(self, pergunta):
        try:
            return str(input(pergunta))
        except:
            print("Digite algum caractere válido!!")
            self.pergunta(pergunta)


def apresentações():
    print(f"Bem Vindo ao jogo da forca\nRegras\nEstes são os recordes:\n{Game.placar}")


class Game:
    placar: list = []
    temas: list[any] = []
    tema_sorteado: any = ""


class Tema:
    # placar: list = []
    # temas: list[str] = ["abluble"]
    # tema_sorteado: str = ""

    def __init__(self, nome: str, palavras: list):
        self.misterio = None
        self.exibido = None
        self.nome = nome
        self.palavras = palavras
        # Game.temas.append(self.nome)
        # print(Game.temas)

    def sortear_palavra(self):
        self.misterio: str = self.palavras[random.randint(0, len(self.palavras))]
        self.exibido: str = "-" * len(self.misterio)

    def __str__(self):
        return self.nome


def sortear_tema(temas: list[str]):
    Game.tema_sorteado = temas[random.randint(0, len(temas) - 1)]
    # print(Game.tema_sorteado)

def criar_temas():
    tema1 = Tema("Animais", ["BURRO", "PORCO", "IGUANA", "SIRI", "HIRAX"])
    tema2 = Tema("Profissões", ["MECANICO", "PINTOR", "CANTOR", "SURFISTA"])
    tema3 = Tema("Paises", ["EGITO", "PERU", "TURQUIA", "ANGOLA", "BRASIL"])
    tema4 = Tema("Nome de mulher bonita", ["ALESSANDRA", "GIOVANNA", "TAÍS", "JULIANA", "ALINE"])
    Game.temas.append(tema1)
    Game.temas.append(tema2)
    Game.temas.append(tema3)
    Game.temas.append(tema4)


def tratamento_str(palavra: str):  # tratar a letra
    return palavra[0].upper


def check(obj: any, scope: any):  # checar vidas e se a letra está na palvra
    if obj in scope:
        return True
    else:
        return False


###Se a letra for errada checa-se as vidas e reinicia

##Em caso de acerto é necessário que conta-se o número de letras na palavra e traduza em pontos, além de uma exibição
# letras perdidas não contam pontos

def editar_palavra(palavra: str, letra: str):  ##edita a palavra
    return palavra.replace("-", letra)


def mensagens(casos: any):
    match (casos):
        case "novo_jogo":
            print(f"Muito bem vamos começar! O tema sorteado é {str(Game.tema_sorteado)}\n")
    pass
