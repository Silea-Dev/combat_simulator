import random as rd

classes = ["espadachim", "mago", "curandeiro", "arqueiro"]
escolhas = ["1", "2", "3", "0"]
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


def verificar_vida(heroi, vilao):
    if heroi["vida"] > 0 and vilao["vida"] > 0:
        return "continua"
    elif vilao["vida"] <= 0 and heroi["vida"] > 0:
        return "vitoria"
    elif heroi["vida"] <= 0 and vilao["vida"] > 0:
        return "derrota"


def acao(escolha):
    if escolha == "0":
        return "exit"
    elif escolha.lower() == "1":
        return "ataque"
    elif escolha.lower() == "2":
        return "defesa"
    elif escolha.lower() == "3":
        return "fugir"


def processar_turno(heroi, vilao, escolha):

    novo_heroi = heroi.copy()
    novo_vilao = vilao.copy()
    mensagem_turno = ""

    acao_str = acao(escolha)

    if acao_str == "ataque":
        ataque_rd = rd.randint(1, 4)
        if ataque_rd == 1:
            dano = novo_heroi["ataque"] - novo_vilao["defesa"]
            dano = max(0, dano)
            novo_vilao["vida"] -= dano
            mensagem_turno = f"Você acertou um ataque crítico! {novo_vilao['nome']} perdeu {dano} de vida."
        else:
            dano_contra_ataque = novo_vilao["ataque"] - novo_heroi["defesa"]
            dano_contra_ataque = max(0, dano_contra_ataque)
            novo_heroi["vida"] -= dano_contra_ataque
            mensagem_turno = f"Você errou o ataque! {novo_vilao['nome']} contra-atacou, causando {dano_contra_ataque} de dano."

    elif acao_str == "defesa":
        defesa_rd = rd.randint(1, 3)
        if defesa_rd == 1:
            novo_heroi["vida"] += 5
            mensagem_turno = f"Defesa bem-sucedida! Você recuperou 5 de vida."
        else:
            dano_recebido = novo_heroi["vida"] * 0.05
            novo_heroi["vida"] -= dano_recebido
            mensagem_turno = f"Sua defesa falhou! Você foi atingido e perdeu {dano_recebido:.0f} de vida."

    elif acao_str == "fugir":
        fugir_rd = rd.randint(1, 5)
        if fugir_rd == 1:
            novo_heroi["status"] = "FUGIU"
            mensagem_turno = "Você fugiu com sucesso!"
        else:
            dano_recebido = novo_heroi["vida"] * 0.10
            novo_heroi["vida"] -= dano_recebido
            mensagem_turno = f"Você não conseguiu fugir e foi atingido, perdendo {dano_recebido:.0f} de vida."

    return novo_heroi, novo_vilao, mensagem_turno
