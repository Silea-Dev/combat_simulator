import random as rd

print("Bem-vindo ao Campo de Batalha!!")
vilao = {"nome": "lucifer", "vida": 500, "ataque": 25, "defesa": 40}


def game():
    print("------Batalha iniciada!------\n")
    while True:
        if heroi["vida"] > 0 and vilao["vida"] > 0:
            choise = input(
                f"O {vilao['nome']} está na sua frente! o que deseja fazer?\nAtacar[1] | Defender[2] | Fugir[3] | end game [0]: "
            )
            if choise == "0":
                print("Obrigado por ter jogado!")
                break
            elif choise.lower() == "1":
                chance_ataque = rd.randint(1, 4)
                if chance_ataque == 1:
                    vilao["vida"] -= heroi["ataque"] - vilao["defesa"]
                    print(f"{vilao['nome']} agora tem {vilao['vida']} de hp")
                    continue
                else:
                    dano_verdadeiro = heroi["defesa"] - vilao["ataque"]
                    if dano_verdadeiro < 0:
                        novo_hp = heroi["vida"] + dano_verdadeiro
                        heroi["vida"] = novo_hp
                    else:
                        print(
                            f"O {vilao['nome']}o não teve dano para te atacar... nossa..."
                        )

                    print(
                        f"------Errooou ataque! {vilao['nome']} lhe contra-atacou!\nNovo hp do heroi: {heroi['vida']}------\n"
                    )
            elif choise.lower() == "2":
                chance_defesa = rd.randint(1, 3)
                if chance_defesa == 1:
                    heroi["vida"] += 5
                    print(
                        f"------Defesa efetuada com sucesso! [ganho de mais 5 de hp!]\nNovo hp: {heroi["vida"]}------\n"
                    )
                    continue
                else:
                    heroi["vida"] *= 95 / 100
                    print(
                        f"------Defesa falhouuuuu! o Boss levou 5% hp!\nNovo hp: {heroi["vida"]}------\n"
                    )
                    continue

            elif choise.lower() == "3":
                chance_fugir = rd.randint(1, 5)
                if chance_fugir == 1:
                    print("------Você fugiu com sucesso!------")
                    break
                else:
                    print(
                        "------Você não conseguiu fugir... o boss lhe acertou de raspão levando 10% hp!------\n"
                    )
                    heroi["vida"] *= 90 / 100
                    continue
        elif heroi["vida"] <= 0 and vilao["vida"] > 0:
            return print("Game over! É uma pena... mas tente novamente!")
        elif vilao["vida"] <= 0 and heroi["vida"] > 0:
            return print(f"PARABÉNS! Você derrotou {vilao['nome']}")


heroi = {}


def coleta_dados():
    while True:
        nome_str = input("Digite o nome de seu personagem: ")
        classe_str = input("Digite a classe de seu personagem: ")
        nivel_str = input("Digite o nível de seu personagem: ")
        hp_str = input("Digite os pontos de vida de seu personagem: ")
        defesa_str = input("Digite os pontos de defesa de seu personagem: ")
        dano_base_str = input("Digite o dano de ataque base de seu personagem: ")
        altura_str = input("Digite a altura (em metros) de seu personagem: ")
        pet_str = input("Seu personagem possuí algum pet [S/N]?\n")
        confirmar_ficha = input(
            f"Deseja confirmar os dados:\n Nome: {nome_str}\n Classe: {classe_str}\n Nível: {nivel_str}\nVida: {hp_str}\n Dano: {dano_base_str}\n Altura: {altura_str}\n Pet: {pet_str}\n[S/N]?\n "
        )
        if confirmar_ficha.lower() == "n":
            print("Refaça a lista [e garanta de preencher todos os dados!]")
            continue
        elif confirmar_ficha.lower() == "s":
            ficha_validada = validar_criar_ficha(
                nome_str,
                classe_str,
                nivel_str,
                hp_str,
                defesa_str,
                dano_base_str,
                altura_str,
                pet_str,
            )
            if ficha_validada is not None:
                return ficha_validada
            else:
                print("[ERROR] níveis, dano, vida, são todos números inteiros!")


def validar_criar_ficha(
    nome_str,
    classe_str,
    nivel_str,
    hp_str,
    defesa_str,
    dano_base_str,
    altura_str,
    pet_str,
):
    try:
        heroi["nome"] = nome_str
        heroi["classe"] = classe_str
        heroi["nivel"] = int(nivel_str)
        heroi["vida"] = int(hp_str)
        heroi["defesa"] = int(defesa_str)
        heroi["ataque"] = int(dano_base_str)
        heroi["altura"] = float(altura_str)
        heroi["pet"] = "sim" if pet_str.lower() == "s" else "não"
        return heroi
    except ValueError:
        return None
