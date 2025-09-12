from core import game, VILAO


while True:
    heroi = {}
    nome_heroi_str = input("Digite o nome de seu heroi!\n")
    confirmar_nome = input(
        f"Deseja confirmar o nome de seu heroi: ({nome_heroi_str}) [S/N]?\n"
    )
    if confirmar_nome.lower() == "s":
        print("iniciando batalha...")
        heroi["nome"] = nome_heroi_str
        heroi["vida"] = 100
        heroi["ataque"] = 50
        heroi["defesa"] = 20
        game(heroi, VILAO)
        break
    else:
        continue
