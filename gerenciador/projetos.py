import gerenciador.services as services
from datetime import datetime

# -----------------------------
# Funções auxiliares
# -----------------------------
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

# -----------------------------
# Menu principal
# -----------------------------
def menu():
    while True:
        print("\n=== GERENCIADOR DE PROJETOS ===")
        print("[1] Cadastrar usuário")
        print("[2] Listar usuários")
        print("[3] Cadastrar projeto")
        print("[4] Listar projetos")
        print("[5] Cadastrar tarefa")
        print("[6] Listar tarefas")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                id = input("ID do usuário: ").strip()
                nome = input("Nome: ").strip()
                email = input("E-mail: ").strip()
                perfil = input("Perfil: ").strip()
                usuario = services.cadastrar_usuario(id, nome, email, perfil)
                print("✅ Usuário cadastrado:", usuario)
            except ValueError as e:
                print("❌ Erro:", e)

        elif opcao == "2":
            usuarios = services.listar_usuarios()
            if usuarios:
                for u in usuarios:
                    print(u)
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "3":
            try:
                id = input("ID do projeto: ").strip()
                nome = input("Nome: ").strip()
                descricao = input("Descrição: ").strip()
                inicio = input_data("Data início (YYYY-MM-DD): ")
                fim = input_data("Data fim (YYYY-MM-DD): ")
                projeto = services.cadastrar_projeto(id, nome, descricao, inicio, fim)
                print("✅ Projeto cadastrado:", projeto)
            except ValueError as e:
                print("❌ Erro:", e)

        elif opcao == "4":
            projetos = services.listar_projetos()
            if projetos:
                for p in projetos:
                    print(p)
            else:
                print("Nenhum projeto cadastrado.")

        elif opcao == "5":
            try:
                id = input("ID da tarefa: ").strip()
                titulo = input("Título: ").strip()
                projeto_id = input("ID do projeto: ").strip()
                responsavel_id = input("ID do responsável: ").strip()
                status = input("Status (pendente/andamento/concluída): ").strip().lower()
                prazo = input_data("Prazo (YYYY-MM-DD): ")
                tarefa = services.cadastrar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo)
                print("✅ Tarefa cadastrada:", tarefa)
            except ValueError as e:
                print("❌ Erro:", e)

        elif opcao == "6":
            tarefas = services.listar_tarefas()
            if tarefas:
                for t in tarefas:
                    print(t)
            else:
                print("Nenhuma tarefa cadastrada.")

        elif opcao == "0":
            print("💾 Encerrando e salvando...")
            break

        else:
            print("❌ Opção inválida, tente novamente.")

# -----------------------------
# Executa o menu
# -----------------------------
if __name__ == "__main__":
    menu()