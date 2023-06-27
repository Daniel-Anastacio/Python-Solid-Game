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
        self.nome = pergunta("Digite seu nome\n")
        self.vidas = 5
        self.pontos = 0
        self.letra: str

    def registrar(self):
        Game.placar.append({self.nome: self.pontos})
        print(Game.placar)

    def resultados(self):
        print(f"{self.nome}, você tem {self.vidas} vidas e {self.pontos} pontos ")

    def pergunta(self, frase: str):
        try:
            return str(input(frase))
        except:
            print("Digite algum caractere válido!!")
            self.pergunta(frase)

    def pontuacao(self, pontos: int):
        self.pontos = self.pontos + pontos

    def punicao(self):
        self.vidas = self.vidas - 1


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
        self.misterio: str = ""
        self.exibido: str = ""
        self.nome = nome
        self.palavras = palavras
        # Game.temas.append(self.nome)
        # print(Game.temas)

    def sortear_palavra(self):
        self.misterio: str = self.palavras[random.randint(0, len(self.palavras) - 1)]
        self.exibido: str = "-" * len(self.misterio)

    def __str__(self):
        return self.nome
def pergunta(frase: str):
    try:
        return str(input(frase))
    except:
        print("Digite algum caractere válido!!")
        pergunta(frase)


def sortear_tema(temas: list[str]):  # USADA
    Game.tema_sorteado = temas[random.randint(0, len(temas) - 1)]
    # print(Game.tema_sorteado)


def criar_temas():  # Usada
    tema1 = Tema("Animais", ["BURRO", "PORCO", "IGUANA", "SIRI", "HIRAX"])
    tema2 = Tema("Profissões", ["MECANICO", "PINTOR", "CANTOR", "SURFISTA"])
    tema3 = Tema("Paises", ["EGITO", "PERU", "TURQUIA", "ANGOLA", "BRASIL"])
    tema4 = Tema("Nome de mulher bonita", ["ALESSANDRA", "GIOVANNA", "TAÍS", "JULIANA", "ALINE"])
    Game.temas.append(tema1)
    Game.temas.append(tema2)
    Game.temas.append(tema3)
    Game.temas.append(tema4)


def tratamento_str(palavra: str):  # tratar a letra
    return palavra[0].upper()


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


##Rotas

def rotas(obj, user):
    obj.letra = tratamento_str(pergunta("Digite um letra:\n"))
    # print(type(Game.tema_sorteado.misterio))
    # print(Game.tema_sorteado.misterio, obj.letra)
    # if "A" in "ANGOLA":
    #     print('é pode ser')
    # else:
    #     print("fudeo")
    if check(obj.letra, Game.tema_sorteado.misterio):
        Game.tema_sorteado.exibido = editar_palavra(Game.tema_sorteado.exibido, obj.letra)
        user.pontuacao(Game.tema_sorteado.misterio.count(obj.letra))
        mensagens("acerto")
    else:
        user.punicao()
        mensagens("erro")


def mensagens(casos: str):
    match casos:
        case "novo_jogo":
            print(f"Muito bem vamos começar! O tema sorteado é {str(Game.tema_sorteado)}")
        case "game!":
            print(
                f"\n{Game.tema_sorteado.exibido}\n{str(Game.tema_sorteado)} - {len(Game.tema_sorteado.exibido)} letras")
        case "acerto":
            print(
                f"Acertaste!\n Existem {Game.tema_sorteado.misterio.count(Game.tema_sorteado.letra)} destas na palavra")
        case "erro":
            print(f"Erraste!\n Anima-te haverão outras oportunidades")
    pass
