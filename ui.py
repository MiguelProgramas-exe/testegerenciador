# ui.py
from users import gerenciador_usuarios
from projetos import gerenciador_projetos
from tarefas import gerenciador_tarefas

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("[1] Usuários")
        print("[2] Projetos")
        print("[3] Tarefas")
        print("[0] Sair")

        try:
            opc = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue

        if opc == 1:
            gerenciador_usuarios()
        elif opc == 2:
            gerenciador_projetos()
        elif opc == 3:
            gerenciador_tarefas()
        elif opc == 0:
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
