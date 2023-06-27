from game import Usuario, Game, criar_temas, sortear_tema, mensagens, tratamento_str, rotas, check

mensagens("apresentações")
player = Usuario()
player.resultados()


def inicio():
    criar_temas()
    sortear_tema(Game.temas)
    mensagens("novo_jogo")
    Game.tema_sorteado.sortear_palavra()


def saida() -> bool:
    if check(Game.tema_sorteado.misterio, Game.tema_sorteado.exibido):
        mensagens("vitória")
        return False
    else:
        return True


def termino(obj) -> bool:
    if check(obj.vidas, range(0, 6)):
        return True
    else:
        mensagens("derrota")
        return False


def main():
    inicio()
    while saida() and termino(player):
        mensagens("game!")
        rotas(Game.tema_sorteado, player)
    player.resultados()
    if (termino(player) or saida()) and check(tratamento_str(player.pergunta("Quer jogar de novo? (S/N)\n")), "S"):
        mensagens("regame")
        main()
    else:
        mensagens("fim")


main()
