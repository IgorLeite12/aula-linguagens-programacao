import os
def limpar_tela():
    """Limpa a tela do console."""
    # Verifica qual sistema operacional está sendo utilizado
    sistema_operacional = os.name

    # Limpa a tela de acordo com o sistema operacional
    if sistema_operacional == "nt":  # Windows
        os.system("cls")
    else:  # Unix/Linux/MacOS
        os.system("clear")

#FUNÇÃO USADA CRIADA PARA LIMPAR {[(CLEAR)]} TIRADA DO CHATGPT