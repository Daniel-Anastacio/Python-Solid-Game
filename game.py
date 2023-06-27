import random
from time import sleep
class Usuario:
    def __init__(self):
        self.nome = pergunta("Digite seu nome\n")
        self.vidas = 5
        self.pontos = 0
        self.letra: str

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



class Game:
    placar: list = []
    temas: list[any] = []
    tema_sorteado: any = ""


class Tema:

    def __init__(self, nome: str, palavras: list):
        self.misterio: str = ""
        self.exibido: str = ""
        self.nome = nome
        self.palavras = palavras

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
    try:
        return palavra[0].upper()
    except:
        print("Valor inválido")


def check(obj: any, scope: any) -> bool:  # checar vidas e se a letra está na palvra
    if obj in scope:
        return True
    else:
        return False


###Se a letra for errada checa-se as vidas e reinicia

##Em caso de acerto é necessário que conta-se o número de letras na palavra e traduza em pontos, além de uma exibição
# letras perdidas não contam pontos

def exibicao(obj: str, letra: str, index: int) -> str:
    obj = list(obj)
    obj[index] = letra
    obj = "".join(obj)
    return obj


def editar_palavra(palavra: str, exibido: str, letra: str) -> str:  ##edita a palavra
    for i in range(0, len(palavra)):
        if check(letra, palavra[i]):
            exibido = exibicao(exibido, letra, i)
        else:
            continue
    return exibido


##Rotas Acerta ou Erra a Letra

def rotas(obj, user) -> None:
    obj.letra = tratamento_str(pergunta("Digite um letra:\n"))
    if check(obj.letra, Game.tema_sorteado.misterio) and not check(obj.letra, Game.tema_sorteado.exibido):
        Game.tema_sorteado.exibido = editar_palavra(Game.tema_sorteado.misterio, Game.tema_sorteado.exibido, obj.letra)
        user.pontuacao(Game.tema_sorteado.misterio.count(obj.letra))
        print(Game.tema_sorteado.exibido)
        mensagens("acerto")
    else:
        user.punicao()
        mensagens("erro")


def mensagens(casos: str):
    sleep(0.25)
    match casos:
        case "apresentações":
            print(f"Bem Vindo ao jogo da forca\nRegras\n")
        case "novo_jogo":
            sleep(0.5)
            print(f"Muito bem vamos começar! O tema sorteado é {str(Game.tema_sorteado)}")
        case "game!":
            print(f"\n{Game.tema_sorteado.exibido}\n{str(Game.tema_sorteado)} - {len(Game.tema_sorteado.exibido)} letras")
        case "acerto":
            print("#"*30, f"\nAcertaste!\nExistem {Game.tema_sorteado.misterio.count(Game.tema_sorteado.letra)} letra(s) desta(s) na palavra\n", "#"*30)
        case "erro":
            print("#"*30, f"\nErraste!\nAnima-te haverão outras oportunidades\n", "#"*30)
        case "derrota":
            print(f"Perdeste!\nBom Jogo! Até uma próxima")
        case "regame":
            sleep(0.5)
            print(f"Então vamos para mais uma rodada")
        case "vitória":
            print(f"Parabéns Você venceu!\nA palavra é {Game.tema_sorteado.misterio}")
        case "fim":
            print(f"Obrigado por jogar!")

    pass


# Condições de Saída ou término
# -Vidas Acabando
# -Jogos Terminando