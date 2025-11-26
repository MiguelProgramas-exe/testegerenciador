import json
import os


ARQUIVO_JSON = "tarefas.json"
pasta_data = "data"
caminho = os.path.join(pasta_data, ARQUIVO_JSON)


# Função: carregar usuários do arquivo JSON
def carregar_tarefas():
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
def salvar_tarefas(lista):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)

def gerenciador_tarefas():
    lista = carregar_tarefas()
    
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("[1] Inserir")
    print("[2] Listar")
    print("[3] Atualizar")
    print("[4] Remover")
    print("[5] Remover TODOS")
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
            titulo = input("Insira o titulo: ").strip()
            responsavel = input("Insira o responsável: ").strip()
            status = input("Insira o status(pendente, andamento, concluída): ").strip() or "user"
            inicio = input("Insira o inicio da tarefa (YYYY-MM-DD): ").strip()
            fim = input("Insira o fim da tarefa (YYYY-MM-DD): ").strip()


            if not titulo:
                print("❌ O título não pode ser vazio.")
                continue
            if not responsavel:
                print("❌ O responsável não pode ser vazio.")
                continue

            novo_usuario = {"título": titulo, "responsável": responsavel, "status": status, "data de início": inicio, "data de entrega": fim }
            lista.append(novo_usuario)
            print("✅ Tarefa registrada com sucesso!")

        # ---------------------------
        # 2 Listar usuários
        # ---------------------------
        elif(opcao==2):
            if not lista:
                print("não há tarefas")
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
            salvar_tarefas(lista)
            print(" Dados salvos com sucesso! Até logo.")
            break

        # ---------------------------
        # Opção inválida
        # ---------------------------
        else:
            print("Opção inválida, tente novamente!")