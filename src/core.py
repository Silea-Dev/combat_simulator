import random as rd

print("Bem-vindo ao Campo de Batalha!!")
vilao = {
    "nome": "lucifer",
    "classe": "demônio",
    "nivel": 100,
    "vida": 2000,
    "ataque": 200,
    "defesa": 150,
    "altura": 5,
    "pet": "dragão",
}
heroi = {}


def coleta_dados():
    while True:
        nome_str = input("Digite o nome de seu personagem: ")
        classe_str = input("Digite a classe de seu personagem: ")
        nivel_str = input("Digite o nível de seu personagem: ")
        hp_str = input("Digite os pontos de vida de seu personagem: ")
        defesa_str = input("Digite os pontos de defesa de seu personagem: ")
        ataque_str = input("Digite o dano de ataque base de seu personagem: ")
        altura_str = input("Digite a altura (em metros) de seu personagem: ")
        pet_str = input("Seu personagem possuí algum pet [S/N]?\n")
        confirmar_ficha = input(
            f"Deseja confirmar os dados:\n Nome: {nome_str}\n Classe: {classe_str}\n Nível: {nivel_str}\nVida: {hp_str}\n Dano: {ataque_str}\n Altura: {altura_str}\n Pet: {pet_str}\n[S/N]?\n "
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
                ataque_str,
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
    ataque_str,
    altura_str,
    pet_str,
):
    try:
        heroi["nome"] = nome_str
        heroi["classe"] = classe_str
        heroi["nivel"] = int(nivel_str)
        heroi["vida"] = int(hp_str)
        heroi["ataque"] = int(ataque_str)
        heroi["defesa"] = int(defesa_str)
        heroi["altura"] = float(altura_str)
        heroi["pet"] = "sim" if pet_str.lower() == "s" else "não"
        return heroi
    except ValueError:
        return None


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
                    dano_verdadeiro = heroi["defesa"] - vilao["ataque"] * 1.02
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
                    heroi["vida"] *= 105 / 100
                    print(
                        f"------Defesa efetuada com sucesso! [ganho de mais 5/100 de hp!]\nNovo hp: {heroi["vida"]}------\n"
                    )
                    continue
                else:
                    heroi["vida"] *= 80 / 100
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
                    heroi["vida"] *= 95 / 100
                    continue
        elif heroi["vida"] <= 0 and vilao["vida"] > 0:
            return print("Game over! É uma pena... mas tente novamente!")
        elif vilao["vida"] <= 0 and heroi["vida"] > 0:
            return print(f"PARABÉNS! Você derrotou {vilao['nome']}")


"""import random as rd

classes = ["espadachim", "mago", "curandeiro", "arqueiro"]

# core
print("Bem-vindo ao Campo de Batalha!!")
# main
vilao = {
    "nome": "lucifer",
    "classe": "demônio",
    # "altura": rd.randint(5, 10),
    "nivel": 100,
    "vida": 500,
    "ataque": 1,
    "defesa": 1,
    "pet": "dragão",
}

VILAO_COPIADO = None
HEROI_COPIADO = None


def solicita_dados():
    classe_str = input("Digite a classe de seu personagem: ")
    return classe_str


def espadachim(classe_str):
    heroi = {
        "classe": classe_str,
        "nivel": 1,
        "vida": 120,
        "defesa": 15,
        "ataque": 10,
    }
    return heroi


def mago(classe_str):
    heroi = {
        "classe": classe_str,
        "nivel": 1,
        "vida": 100,
        "defesa": 8,
        "ataque": 20,
    }
    return heroi


def arqueiro(classe_str):
    heroi = {
        "classe": classe_str,
        "nivel": 1,
        "vida": 100,
        "defesa": 12,
        "ataque": 15,
    }
    return heroi


def curandeiro(classe_str):
    heroi = {
        "classe": classe_str,
        "nivel": 1,
        "vida": 100,
        "defesa": 12,
        "ataque": 15,
    }
    return heroi


def classe_existente(classe_str):
    if classe_str in classes:
        return True
    else:
        return False


def classe_escolhida(classe_str):
    if classe_existente(classe_str):
        if classe_str.lower() == "espadachim":
            return espadachim(classe_str)
        elif classe_str.lower() == "mago":
            return mago(classe_str)
        elif classe_str.lower() == "arqueiro":
            return arqueiro(classe_str)
        elif classe_str.lower() == "curandeiro":
            return curandeiro(classe_str)
    else:
        return None


def verificar_vida(heroi_hp, vilao_hp):
    heroi_hp = HEROI_COPIADO["vida"]
    vilao_hp = VILAO_COPIADO["vida"]
    if heroi_hp > 0 and vilao_hp > 0:
        return "continua"
    elif vilao_hp <= 0 and heroi_hp > 0:
        return True
    elif heroi_hp <= 0 and vilao_hp > 0:
        return False


def condicao_vitoria(heroi_hp, vilao_hp):
    if verificar_vida(heroi_hp, vilao_hp):
        return True
    else:
        return False


def acao(escolha):
    if escolha == "0":
        return "exit"
    elif escolha.lower() == "1":
        return "ataque"
    elif escolha.lower() == "2":
        return "defesa"
    elif escolha.lower() == "3":
        return "fugir"


# def acao_inimigo():


# core
def game():
    print("------Batalha iniciada!------\n")

    while True:
        if verificar_vida(HEROI_COPIADO, VILAO_COPIADO) == "continua":
            escolha = input(
                f"O {vilao['nome']} está na sua frente! o que deseja fazer?\nAtacar[1] | Defender[2] | Fugir[3] | end game[0]: "
            )
            if acao(escolha) == "exit":
                print("Obrigado por ter jogado!")
                return "exit"
            elif acao(escolha) == "ataque":
                chance_ataque = rd.randint(1, 4)
                if chance_ataque == 1:
                    VILAO_COPIADO["vida"] -= (
                        HEROI_COPIADO["ataque"] - VILAO_COPIADO["defesa"]
                    )
                    print(
                        f"{VILAO_COPIADO['nome']} agora tem {VILAO_COPIADO['vida']} de hp"
                    )
                    continue
                else:
                    dano_verdadeiro = HEROI_COPIADO["defesa"] - VILAO_COPIADO["ataque"]
                    if dano_verdadeiro < 0:
                        novo_hp = HEROI_COPIADO["vida"] + dano_verdadeiro
                        HEROI_COPIADO["vida"] = novo_hp
                    else:
                        print(
                            f"O {VILAO_COPIADO['nome']}o não teve dano para te atacar... nossa..."
                        )
                    print(
                        f"------Errooou ataque! {VILAO_COPIADO['nome']} lhe contra-atacou!\nNovo hp do heroi: {HEROI_COPIADO['vida']}------\n"
                    )
            elif escolha.lower() == "2":
                chance_defesa = rd.randint(1, 3)
                if chance_defesa == 1:
                    HEROI_COPIADO["vida"] += 5
                    print(
                        f"------Defesa efetuada com sucesso! [ganho de mais 5 de hp!]\nNovo hp: {heroi["vida"]}------\n"
                    )
                    continue
                else:
                    HEROI_COPIADO["vida"] *= 95 / 100
                    print(
                        f"------Defesa falhouuuuu! o Boss levou 5% hp!\nNovo hp: {HEROI_COPIADO["vida"]}------\n"
                    )
                    continue

            elif escolha.lower() == "3":
                chance_fugir = rd.randint(1, 5)
                if chance_fugir == 1:
                    print("------Você fugiu com sucesso!------")
                    break
                else:
                    print(
                        "------Você não conseguiu fugir... o boss lhe acertou de raspão levando 10% hp!------\n"
                    )
                    HEROI_COPIADO["vida"] *= 90 / 100
                    continue
        elif HEROI_COPIADO["vida"] <= 0 and VILAO_COPIADO["vida"] > 0:
            return print("Game over! É uma pena... mas tente novamente!")
        elif VILAO_COPIADO["vida"] <= 0 and HEROI_COPIADO["vida"] > 0:
            return print(f"PARABÉNS! Você derrotou {VILAO_COPIADO['nome']}")


print("-----Jogo iniciado!-----")


if __name__ == "__main__":
    dados = solicita_dados()
    heroi_escolhido = classe_escolhida(dados)
    if heroi_escolhido is not None:
        HEROI_COPIADO = heroi_escolhido.copy()
        VILAO_COPIADO = vilao.copy()
        print(HEROI_COPIADO)
    else:
        print("escolha uma classe!")

    verificar_vida(HEROI_COPIADO, VILAO_COPIADO)
    naosei = verificar_vida(HEROI_COPIADO, VILAO_COPIADO)
    game()


"""
