# tarefas.py
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

def gerenciador_tarefas():
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
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
            id= input("ID do projeto: ").strip()
            nome = input("titulo: ").strip()
            descricao = input("status: ").strip()

            inicio = input_data("Data de início (YYYY-MM-DD): ")
            fim = input_data("Data de fim (YYYY-MM-DD): ")

            # valida fim >= inicio
            while datetime.strptime(fim, "%Y-%m-%d") < datetime.strptime(inicio, "%Y-%m-%d"):
                print("❌ Data de fim não pode ser anterior à data de início.")
                fim = input_data("Data de fim (YYYY-MM-DD): ")

            try:
                projeto = services.cadastrar_projeto(id, nome, descricao, inicio, fim)
                print("✅ Tarefa registrada com sucesso!")
                print(projeto)
            except ValueError as e:
                print("❌", e)

        elif opcao == 2:
            projetos = services.listar_projetos()
            if not projetos:
                print("Não há tarefas cadastradas.")
            else:
                print("\n--- Lista de Tarefas ---")
                for p in projetos:
                    print(f"titulo: {p['nome']} | ID: {p['id']} | status: {p['descricao']} | Início: {p['inicio']} | Fim: {p['fim']}")
                print("-------------------------")

        elif opcao == 3:
            busca = input("Digite parte do nome para buscar: ").strip().lower()
            encontrados = [p for p in services.listar_projetos() if busca in p["nome"].lower()]
            if encontrados:
                print("✅ Tarefa encontrada:")
                for p in encontrados:
                    print(f"- {p['nome']} | ID: {p['id']} | status: {p['descricao']}")
            else:
                print("❌ Nenhum projeto encontrado!")

        elif opcao == 4:
            nome_busca = input("Digite o nome exato da tarefa para atualizar: ").strip()
            projeto = next((p for p in services.listar_projetos() if p["nome"].lower() == nome_busca.lower()), None)
            if not projeto:
                print("❌ tarefa não encontrado!")
                continue

            print("tarefa atual:", projeto)
            novo_nome = input("Novo titulo (vazio para manter): ").strip() or None
            nova_desc = input("Novo status (vazio para manter): ").strip() or None

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
                print("✅ Tarefa removida:", removido)
            else:
                print("❌ Tarefa não encontrada!")

        elif opcao == 6:
            confirma = input("Tem certeza que deseja remover TODAS as tarefas? (s/n): ").strip().lower()
            if confirma == "s":
                services.remover_todos_projetos()
                print("✅ Todos as tarefas removidas.")
            else:
                print("Operação cancelada.")

        elif opcao == 0:
            break
        else:
            print("❌ Opção inválida. Tente novamente!")
