from users import gerenciador_usuarios
from projetos import gerenciador_projetos
while True:
    print("\n=== GERENCIADOR ===")
    print("[1] Usuários")
    print("[2] Projetos")
    print("[3] Tarefas")
    print("[0] Sair")
    try:
        opcao = int(input("Digite o que deseja fazer: "))
    except ValueError:
        print("❌ Opção inválida, digite um número!")
        continue

    if opcao == 1:
        gerenciador_usuarios()

    elif(opcao==2):
        gerenciador_projetos()


    elif opcao == 3:
        

    elif opcao == 0:
        print(" Salvando e encerrando...")
        salvar_usuarios(lista)
        print(" Dados salvos com sucesso! Até logo.")
        break
    else:
        print("Opção inválida, tente novamente!")

