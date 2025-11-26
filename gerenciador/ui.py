import services
from datetime import datetime


def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def input_data(prompt):
    while True:
        data = input(prompt).strip()
        if validar_data(data):
            return data
        print("❌ Formato inválido! Use YYYY-MM-DD.")


def menu():
    while True:
        print("\n=== GERENCIADOR DE PROJETOS ===")
        print("[1] Cadastrar usuário")
        print("[2] Listar usuários")
        print("[3] Atualizar usuário")
        print("[4] Remover usuário")
        print("[5] Cadastrar projeto")
        print("[6] Listar projetos")
        print("[7] Atualizar projeto")
        print("[8] Remover projeto")
        print("[9] Cadastrar tarefa")
        print("[10] Listar tarefas")
        print("[11] Atualizar tarefa")
        print("[12] Remover tarefa")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        # ---------------- USUÁRIOS ----------------

        if opcao == "1":
            try:
                id = input("ID do usuário: ").strip()
                nome = input("Nome: ").strip()
                email = input("E-mail: ").strip()
                perfil = input("Perfil: ").strip()
                u = services.cadastrar_usuario(id, nome, email, perfil)
                print("✅ Usuário cadastrado:", u)
            except ValueError as e:
                print("❌", e)

        elif opcao == "2":
            usuarios = services.listar_usuarios()
            print("\n--- Usuários ---")
            if usuarios:
                for u in usuarios:
                    print(u)
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "3":
            email = input("Email do usuário a atualizar: ").strip()
            novo_nome = input("Novo nome (vazio para manter): ").strip()
            novo_email = input("Novo email (vazio para manter): ").strip()
            novo_perfil = input("Novo perfil (vazio para manter): ").strip()
            u = services.atualizar_usuario(email, novo_nome, novo_email, novo_perfil)
            if u:
                print("✅ Atualizado:", u)
            else:
                print("❌ Usuário não encontrado")

        elif opcao == "4":
            email = input("Email do usuário a remover: ").strip()
            u = services.remover_usuario(email)
            if u:
                print("✅ Removido:", u)
            else:
                print("❌ Usuário não encontrado")

        # ---------------- PROJETOS ----------------

        elif opcao == "5":
            try:
                id = input("ID projeto: ").strip()
                nome = input("Nome: ").strip()
                desc = input("Descrição: ").strip()
                inicio = input_data("Data início YYYY-MM-DD: ")
                fim = input_data("Data fim YYYY-MM-DD: ")
                p = services.cadastrar_projeto(id, nome, desc, inicio, fim)
                print("✅ Projeto cadastrado:", p)
            except ValueError as e:
                print("❌", e)

        elif opcao == "6":
            projetos = services.listar_projetos()
            print("\n--- Projetos ---")
            if projetos:
                for p in projetos:
                    print(p)
            else:
                print("Nenhum projeto cadastrado.")

        elif opcao == "7":
            nome = input("Nome do projeto a atualizar: ").strip()
            novo_nome = input("Novo nome (vazio para manter): ").strip()
            nova_desc = input("Nova descrição (vazio para manter): ").strip()
            novo_inicio = input("Nova data início YYYY-MM-DD (vazio para manter): ").strip()
            novo_fim = input("Nova data fim YYYY-MM-DD (vazio para manter): ").strip()

            p = services.atualizar_projeto(
                nome,
                novo_nome,
                nova_desc,
                novo_inicio if validar_data(novo_inicio) else None,
                novo_fim if validar_data(novo_fim) else None
            )

            if p:
                print("✅ Atualizado:", p)
            else:
                print("❌ Projeto não encontrado")

        elif opcao == "8":
            nome = input("Nome do projeto a remover: ").strip()
            p = services.remover_projeto(nome)
            if p:
                print("✅ Removido:", p)
            else:
                print("❌ Projeto não encontrado")

        # ---------------- TAREFAS ----------------

        elif opcao == "9":
            try:
                id = input("ID tarefa: ").strip()
                titulo = input("Título: ").strip()
                projeto_id = input("ID projeto: ").strip()
                responsavel_id = input("ID usuário: ").strip()
                status = input("Status (pendente/andamento/concluída): ").strip().lower()
                prazo = input_data("Prazo YYYY-MM-DD: ")

                t = services.cadastrar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo)
                print("✅ Tarefa cadastrada:", t)
            except ValueError as e:
                print("❌", e)

        elif opcao == "10":
            tarefas = services.listar_tarefas()
            print("\n--- Tarefas ---")
            if tarefas:
                for t in tarefas:
                    print(t)
            else:
                print("Nenhuma tarefa cadastrada.")

        elif opcao == "11":
            id = input("ID da tarefa a atualizar: ").strip()
            novo_titulo = input("Novo título (vazio para manter): ").strip()
            novo_status = input("Novo status (vazio para manter): ").strip()
            novo_prazo = input("Novo prazo YYYY-MM-DD (vazio para manter): ").strip()

            t = services.atualizar_tarefa(
                id,
                novo_titulo,
                novo_status,
                novo_prazo if validar_data(novo_prazo) else None
            )

            if t:
                print("✅ Atualizado:", t)
            else:
                print("❌ Tarefa não encontrada")

        elif opcao == "12":
            id = input("ID da tarefa a remover: ").strip()
            t = services.remover_tarefa(id)
            if t:
                print("✅ Removido:", t)
            else:
                print("❌ Tarefa não encontrada")

        # ---------------- SAIR ----------------

        elif opcao == "0":
            print("💾 Encerrando...")
            break

        else:
            print("❌ Opção inválida!")
