# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import random
#
# ps = ["CAVALO", "CACHORRO", "HIENA", "FAISAO",'ARARA', 'HIPOPÓTAMO', 'HIRAX', 'TARTIGRADO']
# ps = ps[random.randint(0, (len(ps)-1))]
# vidas = 3
# pontuação = 0
# listchec = []
# listchec2 = []
#
# while vidas > 0 and pontuação < len(ps):
#   print('JOGO DA FORCA\nTEMA: ANIMAIS')
#   print(f'A palavra tem {len(ps)} letras')
#   letra = input('digite uma letra:\n')
#   letra=letra.upper()
#   if ps.count(letra) == 0:
#     vidas = vidas - 1
#     listchec2.append(letra)
#     print(f"Esta letra não está na palavra secreta\nNúmero de vidas: {vidas}\nPontuação necessária para vencer: {len(ps)}\nPontuação atual: {pontuação}\nLetras Erradas: {str(listchec2)}\n")
#   else:
#     pontuação = pontuação + ps.count(letra)
#     print(f'Essa letra aparece {ps.count(letra)} vez(es)\nnúmero de vidas: {vidas}\npontuação necessária para vencer: {len(ps)}\npontuação atual: {pontuação}\nLetras Erradas: {listchec2}\n')
#     for x in range (0, (len(ps))):
#       if letra == ps[x]:
#         print(ps[x])
#         listchec.append(ps[x])
#       elif letra != ps[x] and ps[x] in listchec:
#         print(ps[x])
#       else:
#         print('----')
# if pontuação == len(ps):
#   print(f"Parabéns você venceu a palavra correta é {ps}")
# elif vidas == 0:
#   print('Sua vidas chegaram a zero você perdeu')


from geral import apresentações, Usuario

def main():
  apresentações()
  player = Usuario()
  player.registrar()
  player.resultados()


def loop():
    pass

main()