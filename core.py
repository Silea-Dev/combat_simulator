import random as rd

print("Bem-vindo ao Campo de Batalha!!")


def game(heroi, vilao):
    print("------Batalha iniciada!------\n")
    if heroi["vida"] > 0 and vilao["vida"] > 0:
        while True:
            choise = input(
                f"O {vilao['nome']} está na sua frente! o que deseja fazer?\nAtacar[1] | Defender[2] | Fugir[3] | end game [0]: "
            )
            if choise == "0":
                print("Obrigado por ter jogado!")
                break
            elif choise.lower() == "1":
                chance_ataque = rd.randint(1, 4)
                if chance_ataque == 1:
                    dano_total = heroi["ataque"] - vilao["defesa"]
                    vilao["vida"] -= heroi["ataque"] - vilao["defesa"]
                    print(
                        f"O dano dado foi de: {dano_total}\n{vilao['nome']} agora tem {vilao['vida']} hp"
                    )
                    continue
                else:
                    novo_hp = heroi["vida"] + heroi["defesa"] - vilao["ataque"]
                    heroi["vida"] = novo_hp
                    print(
                        f"------Errooou ataque! {vilao['nome']} lhe contra-atacou!\nNovo hp do heroi: {novo_hp}------\n"
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
    elif heroi["vida"] <= 0:
        print("Game over! É uma pena... mas tente novamente!")
    elif vilao["vida"] <= 0:
        print(f"PARABÉNS! Você derrotou {vilao['nome']}")
