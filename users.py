import json
import os


ARQUIVO_JSON = "usuarios.json"
pasta_data = "data"
caminho = os.path.join(pasta_data, ARQUIVO_JSON)


# Função: carregar usuários do arquivo JSON
def carregar_usuarios():
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)
                if isinstance(dados, list):
                    return dados
            except json.JSONDecodeError:
                pass
    return []


# Função: salvar usuários no arquivo JSON
def salvar_usuarios(lista):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)

def gerenciador_usuarios():
# Carrega usuários existentes (ou lista vazia)
    lista = carregar_usuarios()


# Loop principal do menu
    print("\n=== GERENCIADOR DE USUÁRIOS ===")
    print("[1] Inserir")
    print("[2] Listar")
    print("[3] Buscar")
    print("[4] Atualizar email e perfil")
    print("[5] Remover")
    print("[6] Remover TODOS")
    print("[0] Sair")
    while True:

        try:
            opcao = int(input("Digite o que deseja fazer: "))
        except ValueError:
            print("❌ Opção inválida, digite um número!")
            continue

        # ---------------------------
        # 1 Inserir novo usuário
        # ---------------------------
        if opcao == 1:
            nome = input("Insira o nome: ").strip()
            email = input("Insira o email: ").strip()
            perfil = input("Insira o perfil: ").strip() or "user"

            if not nome:
                print("❌ O nome não pode ser vazio.")
                continue
            if not email:
                print("❌ O email não pode ser vazio.")
                continue
            if any(u["email"].lower() == email.lower() for u in lista):
                print("❌ Este e-mail já está cadastrado!")
                continue

            novo_usuario = {"nome": nome, "email": email, "perfil": perfil}
            lista.append(novo_usuario)
            print("✅ Usuário inserido com sucesso!")

        # ---------------------------
        # 2 Listar usuários
        # ---------------------------
        elif(opcao==2):
            if not lista:
                print("não há usuários")
                opcao=10
            else:
                for a in lista:
                    print(a)
            opcao=10

        # ---------------------------
        # 3 Buscar usuário por nome (parcial)
        # ---------------------------
        elif opcao == 3:
            busca = input("Digite parte do nome para buscar: ").strip().lower()
            encontrados = [u for u in lista if busca in u["nome"].lower()]
            if encontrados:
                print("✅ Usuários encontrados:")
                for u in encontrados:
                    print(f"- {u['nome']} ({u['email']}) - Perfil: {u['perfil']}")
            else:
                print("❌ Nenhum usuário encontrado!")

        # ---------------------------
        # 4 Atualizar email e perfil
        # ---------------------------
        elif opcao == 4:
            busca = input("Digite o nome exato do usuário que deseja alterar: ").strip()
            encontrado = False
            for usuario in lista:
                if usuario["nome"].lower() == busca.lower():
                    print("Usuário atual:", usuario)
                    novo_email = input("Novo email (vazio para manter): ").strip()
                    novo_perfil = input("Novo perfil (vazio para manter): ").strip()

                    if novo_email and any(u["email"].lower() == novo_email.lower() and u != usuario for u in lista):
                        print("❌ Este email já está em uso!")
                        break

                    if novo_email:
                        usuario["email"] = novo_email
                    if novo_perfil:
                        usuario["perfil"] = novo_perfil

                    print("Dados atualizados com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("Usuário não encontrado!")

        # ---------------------------
        # 5 Remover um usuário
        # ---------------------------
        elif opcao == 5:
            remov = input("Digite o nome do usuário que deseja excluir: ").strip()
            for i, novo_usuario in enumerate(lista):
                if novo_usuario["nome"].lower() == remov.lower():
                    print(" Usuário removido:", novo_usuario)
                    lista.pop(i)
                    break
            else:
                print("Usuário não encontrado!")

        # ---------------------------
        # 6 Remover todos os usuários
        # ---------------------------
        elif opcao == 6:
            confirma = input("Tem certeza que deseja remover TODOS os usuários? (s/n): ").lower()
            if confirma == "s":
                lista.clear()
                print("Todos os usuários foram removidos!")
            else:
                print("Operação cancelada.")

        # ---------------------------
        # 0 Sair e salvar
        # ---------------------------
        elif opcao == 0:
            print(" Salvando e encerrando...")
            salvar_usuarios(lista)
            print(" Dados salvos com sucesso! Até logo.")
            break

        # ---------------------------
        # Opção inválida
        # ---------------------------
        else:
            print("Opção inválida, tente novamente!")