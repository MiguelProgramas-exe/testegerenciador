# projetos.py
import services
from datetime import datetime

def validar_data(data_str):
    try:
        datetime.strptime(data_str.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False

def input_data(prompt):
    while True:
        s = input(prompt).strip()
        if validar_data(s):
            return s
        print("❌ Data inválida. Use o formato YYYY-MM-DD.")

def gerenciador_projetos():
    while True:
        print("\n=== GERENCIADOR DE PROJETOS ===")
        print("[1] Inserir")
        print("[2] Listar")
        print("[3] Buscar")
        print("[4] Atualizar")
        print("[5] Remover")
        print("[6] Remover TODOS")
        print("[0] Sair")
        try:
            opcao = int(input("Digite o que deseja fazer: "))
        except ValueError:
            print("❌ Opção inválida, digite um número!")
            continue

        if opcao == 1:
            id_projeto = input("ID do projeto: ").strip()
            nome = input("Nome do projeto: ").strip()
            descricao = input("Descrição: ").strip()

            inicio = input_data("Data de início (YYYY-MM-DD): ")
            fim = input_data("Data de fim (YYYY-MM-DD): ")

            # valida fim >= inicio
            while datetime.strptime(fim, "%Y-%m-%d") < datetime.strptime(inicio, "%Y-%m-%d"):
                print("❌ Data de fim não pode ser anterior à data de início.")
                fim = input_data("Data de fim (YYYY-MM-DD): ")

            try:
                projeto = services.cadastrar_projeto(id_projeto, nome, descricao, inicio, fim)
                print("✅ Projeto cadastrado com sucesso!")
                print(projeto)
            except ValueError as e:
                print("❌", e)

        elif opcao == 2:
            projetos = services.listar_projetos()
            if not projetos:
                print("Não há projetos cadastrados.")
            else:
                print("\n--- Lista de Projetos ---")
                for p in projetos:
                    print(f"Nome: {p['nome']} | ID: {p['id']} | Descrição: {p['descricao']} | Início: {p['inicio']} | Fim: {p['fim']}")
                print("-------------------------")

        elif opcao == 3:
            busca = input("Digite parte do nome para buscar: ").strip().lower()
            encontrados = [p for p in services.listar_projetos() if busca in p["nome"].lower()]
            if encontrados:
                print("✅ Projetos encontrados:")
                for p in encontrados:
                    print(f"- {p['nome']} | ID: {p['id']} | Descrição: {p['descricao']}")
            else:
                print("❌ Nenhum projeto encontrado!")

        elif opcao == 4:
            nome_busca = input("Digite o nome exato do projeto para atualizar: ").strip()
            projeto = next((p for p in services.listar_projetos() if p["nome"].lower() == nome_busca.lower()), None)
            if not projeto:
                print("❌ Projeto não encontrado!")
                continue

            print("Projeto atual:", projeto)
            novo_nome = input("Novo nome (vazio para manter): ").strip() or None
            nova_desc = input("Nova descrição (vazio para manter): ").strip() or None

            novo_inicio = input("Nova data de início (YYYY-MM-DD) ou vazio para manter: ").strip()
            if novo_inicio:
                while not validar_data(novo_inicio):
                    print("❌ Data inválida.")
                    novo_inicio = input("Nova data de início (YYYY-MM-DD) ou vazio para manter: ").strip()
            else:
                novo_inicio = None

            novo_fim = input("Nova data de fim (YYYY-MM-DD) ou vazio para manter: ").strip()
            if novo_fim:
                while not validar_data(novo_fim):
                    print("❌ Data inválida.")
                    novo_fim = input("Nova data de fim (YYYY-MM-DD) ou vazio para manter: ").strip()
            else:
                novo_fim = None

            # checar relação entre datas se ambas fornecidas
            data_inicio_final = novo_inicio or projeto["inicio"]
            data_fim_final = novo_fim or projeto["fim"]
            if datetime.strptime(data_fim_final, "%Y-%m-%d") < datetime.strptime(data_inicio_final, "%Y-%m-%d"):
                print("❌ Data final não pode ser anterior à data de início. Operação cancelada.")
                continue

            try:
                atualizado = services.atualizar_projeto(nome_busca, novo_nome, nova_desc, novo_inicio, novo_fim)
                print("✅ Projeto atualizado:", atualizado)
            except ValueError as e:
                print("❌", e)

        elif opcao == 5:
            nome_remover = input("Digite o nome do projeto a remover: ").strip()
            removido = services.remover_projeto(nome_remover)
            if removido:
                print("✅ Projeto removido:", removido)
            else:
                print("❌ Projeto não encontrado!")

        elif opcao == 6:
            confirma = input("Tem certeza que deseja remover TODOS os projetos? (s/n): ").strip().lower()
            if confirma == "s":
                services.remover_todos_projetos()
                print("✅ Todos os projetos removidos.")
            else:
                print("Operação cancelada.")

        elif opcao == 0:
            break
        else:
            print("❌ Opção inválida. Tente novamente!")
