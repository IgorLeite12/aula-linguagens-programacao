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


senha = input("Digite sua senha: ")
limpar_tela()
conf = input("Repita sua senha: ")

while conf != senha:
    limpar_tela()
    input("Senha incorreta! Digite novamente: ")