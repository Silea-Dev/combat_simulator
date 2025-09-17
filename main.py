from src.core import (
    VILAO_COPIADO,
    HEROI_COPIADO,
    vilao,
    escolhas,
    verificar_vida,
    acao,
    copias_H_V,
)
import random as rd


print("-----Jogo iniciado!-----")


if __name__ == "__main__":
    copia = copias_H_V()
    print("------Batalha iniciada!------\n")

    while True:
        escolha = input(
            f"O {vilao['nome']} está na sua frente! o que deseja fazer?\nAtacar[1] | Defender[2] | Fugir[3] | end game[0]: "
        )
        if escolha in escolhas:
            vida_atual = verificar_vida()
            if vida_atual == "continua":
                if acao(escolha) == "exit":
                    print("Obrigado por ter jogado!")
                    break
                elif acao(escolha) == "ataque":
                    #################################################################################################
                    ataque_rd = rd.randint(1, 4)
                    if ataque_rd == 1:
                        vida_atual_vilao = VILAO_COPIADO["vida"] - (
                            HEROI_COPIADO["ataque"] - VILAO_COPIADO["defesa"]
                        )
                        VILAO_COPIADO["vida"] = vida_atual_vilao
                        print(
                            f"{VILAO_COPIADO['nome']} agora tem {vida_atual_vilao} de hp"
                        )
                    else:
                        vida_atual_heroi = HEROI_COPIADO["vida"] - (
                            VILAO_COPIADO["ataque"] - HEROI_COPIADO["defesa"]
                        )

                        HEROI_COPIADO["vida"] = vida_atual_heroi

                        print(
                            f"------Errooou ataque! {VILAO_COPIADO['nome']} lhe contra-atacou!\nNovo hp do heroi: {vida_atual_heroi}------\n"
                        )
                ################################################################################################################################
                elif acao(escolha) == "defesa":
                    defesa_rd = rd.randint(1, 3)
                    if defesa_rd == 1:
                        HEROI_COPIADO["vida"] += 5
                        print(
                            f"------Defesa efetuada com sucesso! [ganho de mais 5 de hp!]\nNovo hp: {HEROI_COPIADO["vida"]}------\n"
                        )
                    else:
                        HEROI_COPIADO["vida"] *= 95 / 100
                        print(
                            f"------Defesa falhouuuuu! o Boss levou 5% hp!\nNovo hp: {HEROI_COPIADO["vida"]}------\n"
                        )
                ################################################################################################################################
                elif acao(escolha) == "fugir":
                    fugir_rd = rd.randint(1, 5)
                    if fugir_rd == 1:
                        print("------Você fugiu com sucesso!------")
                        break
                    else:
                        HEROI_COPIADO["vida"] *= 90 / 100
                        print(
                            f"------Você não conseguiu fugir... o boss lhe acertou de raspão levando 10% hp!------\nNovo hp: {HEROI_COPIADO["vida"]}"
                        )

            #########################################################################################################
            # CONDIÇÃO DE VITÓRIA
            elif verificar_vida() == "derrota":
                print("Game over! É uma pena... mas tente novamente!")
                break

            elif verificar_vida() == "vitoria":
                print(f"PARABÉNS! Você derrotou {vilao['nome']}")
                break

        else:
            print("[ERROR] Escolha uma dentre as ações!\n")
            continue
"""import random as rd

# core
classes = ["espadachim", "mago", "curandeiro", "arqueiro"]
escolhas = ["1", "2", "3", "0"]
print("Bem-vindo ao Campo de Batalha!!")
vilao = {
    "nome": "lucifer",
    "classe": "demônio",
    "nivel": 100,
    "vida": 500,
    "ataque": 20,
    "defesa": 10,
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


def verificar_vida():
    if HEROI_COPIADO["vida"] > 0 and VILAO_COPIADO["vida"] > 0:
        return "continua"
    elif VILAO_COPIADO["vida"] <= 0 and HEROI_COPIADO["vida"] > 0:
        return "vitoria"
    elif HEROI_COPIADO["vida"] <= 0 and VILAO_COPIADO["vida"] > 0:
        return "derrota"


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


print("-----Jogo iniciado!-----")

# main
if __name__ == "__main__":
    dados = solicita_dados()
    heroi_escolhido = classe_escolhida(dados)
    if heroi_escolhido is not None:
        HEROI_COPIADO = heroi_escolhido.copy()
        VILAO_COPIADO = vilao.copy()
        print(HEROI_COPIADO)
        heroi_hp = HEROI_COPIADO["vida"]
        vilao_hp = VILAO_COPIADO["vida"]
    else:
        print("escolha uma classe!")

    ################################################################################################################################
    print("------Batalha iniciada!------\n")

    while True:
        escolha = input(
            f"O {vilao['nome']} está na sua frente! o que deseja fazer?\nAtacar[1] | Defender[2] | Fugir[3] | end game[0]: "
        )
        if escolha in escolhas:
            vida_atual = verificar_vida()
            if vida_atual == "continua":
                if acao(escolha) == "exit":
                    print("Obrigado por ter jogado!")
                    break
                elif acao(escolha) == "ataque":
                    ################################################################################################################################
                    ataque_rd = rd.randint(1, 4)
                    if ataque_rd == 1:
                        vida_atual_vilao = VILAO_COPIADO["vida"] - (
                            HEROI_COPIADO["ataque"] - VILAO_COPIADO["defesa"]
                        )
                        VILAO_COPIADO["vida"] = vida_atual_vilao
                        print(
                            f"{VILAO_COPIADO['nome']} agora tem {vida_atual_vilao} de hp"
                        )
                    else:
                        vida_atual_heroi = HEROI_COPIADO["vida"] - (
                            VILAO_COPIADO["ataque"] - HEROI_COPIADO["defesa"]
                        )

                        HEROI_COPIADO["vida"] = vida_atual_heroi

                        print(
                            f"------Errooou ataque! {VILAO_COPIADO['nome']} lhe contra-atacou!\nNovo hp do heroi: {vida_atual_heroi}------\n"
                        )
                ################################################################################################################################
                elif acao(escolha) == "defesa":
                    defesa_rd = rd.randint(1, 3)
                    if defesa_rd == 1:
                        HEROI_COPIADO["vida"] += 5
                        print(
                            f"------Defesa efetuada com sucesso! [ganho de mais 5 de hp!]\nNovo hp: {HEROI_COPIADO["vida"]}------\n"
                        )
                    else:
                        HEROI_COPIADO["vida"] *= 95 / 100
                        print(
                            f"------Defesa falhouuuuu! o Boss levou 5% hp!\nNovo hp: {HEROI_COPIADO["vida"]}------\n"
                        )
                ################################################################################################################################
                elif acao(escolha) == "fugir":
                    fugir_rd = rd.randint(1, 5)
                    if fugir_rd == 1:
                        print("------Você fugiu com sucesso!------")
                        break
                    else:
                        HEROI_COPIADO["vida"] *= 90 / 100
                        print(
                            f"------Você não conseguiu fugir... o boss lhe acertou de raspão levando 10% hp!------\nNovo hp: {HEROI_COPIADO["vida"]}"
                        )

            ################################################################################################################################
            # CONDIÇÃO DE VITÓRIA
            elif verificar_vida() == "derrota":
                print("Game over! É uma pena... mas tente novamente!")
                break

            elif verificar_vida() == "vitoria":
                print(f"PARABÉNS! Você derrotou {vilao['nome']}")
                break

        else:
            print("[ERROR] Escolha uma dentre as ações!\n")
            continue
"""
