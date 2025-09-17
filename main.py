from src import core as cr
import random as rd

if __name__ == "__main__":
    print("Bem-vindo ao Campo de Batalha!!")
    dados = cr.solicita_dados()
    heroi_escolhido = cr.classe_escolhida(dados)
    if heroi_escolhido is not None:
        HEROI_COPIADO = heroi_escolhido.copy()
        VILAO_COPIADO = cr.vilao.copy()
        print(HEROI_COPIADO)
        heroi_hp = HEROI_COPIADO["vida"]
        vilao_hp = VILAO_COPIADO["vida"]
    else:
        print("escolha uma classe!")

    print("------Batalha iniciada!------\n")

    while True:
        escolha = input(
            f"O {cr.vilao['nome']} está na sua frente! o que deseja fazer?\nAtacar[1] | Defender[2] | Fugir[3] | end game[0]: "
        )
        if escolha == "0":
            break
        elif escolha in cr.escolhas:
            vida_atual = cr.verificar_vida(HEROI_COPIADO, VILAO_COPIADO)
            if vida_atual == "continua":
                HEROI_COPIADO, VILAO_COPIADO, mensagem = cr.processar_turno(
                    HEROI_COPIADO, VILAO_COPIADO, escolha
                )
                print(mensagem)
            # CONDIÇÃO DE VITÓRIA
            elif cr.verificar_vida(HEROI_COPIADO, VILAO_COPIADO) == "derrota":
                print("Game over! É uma pena... mas tente novamente!")
                break

            elif cr.verificar_vida(HEROI_COPIADO, VILAO_COPIADO) == "vitoria":
                print(f"PARABÉNS! Você derrotou {cr.vilao['nome']}")
                break

        else:
            print("[ERROR] Escolha uma dentre as ações!\n")
            continue
