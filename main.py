from src.core import game, vilao, coleta_dados, heroi


while True:
    saida = input("Deseja criar uma ficha de personagem[S/N]?\n")
    if saida.lower() == "s":
        nova_ficha = coleta_dados()
        print(heroi)
        game()
        break
    elif saida.lower() == "n":
        print("Sem ficha, sem jogo. Volte quando quiser realmente jogar!")
        break
    else:
        continue
