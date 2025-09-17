import random as rd

classes = ["espadachim", "mago", "curandeiro", "arqueiro"]
escolhas = ["1", "2", "3", "0"]
VILAO_COPIADO = None
HEROI_COPIADO = None
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


def copias_H_V():
    dados = solicita_dados()
    heroi_escolhido = classe_escolhida(dados)
    if heroi_escolhido is not None:
        HEROI_COPIADO = heroi_escolhido.copy()
        VILAO_COPIADO = vilao.copy()
        heroi_hp = HEROI_COPIADO["vida"]
        vilao_hp = VILAO_COPIADO["vida"]
        return heroi_hp, vilao_hp


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
