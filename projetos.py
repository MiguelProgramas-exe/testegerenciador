import json
import os


ARQUIVO_JSON = "projetos.json"
pasta_data = "data"
caminho = os.path.join(pasta_data, ARQUIVO_JSON)


# Função: carregar projetos do arquivo JSON
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


# Função: salvar projetos no arquivo JSON
def salvar_usuarios(lista):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)


# Carrega projetos existentes (ou lista vazia)
lista = carregar_usuarios()


# Loop principal do menu
print("\n=== GERENCIADOR DE projetoS ===")
print("[1] Inserir")
print("[2] Listar")
print("[3] Buscar")
print("[4] Atualizar id e descrição")
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
    # 1 Inserir novo projeto
    # ---------------------------
    if opcao == 1:
        nome = input("Insira o nome do projeto: ").strip()
        id = input("Insira o id do projeto: ").strip()
        descrição = input("Insira a descrição do projeto: ").strip() or "user"
        inicio = input("Insira o inicio do projeto (YYYY-MM-DD): ").strip()
        fim = input("Insira o fim do projeto (YYYY-MM-DD): ").strip()

        if not nome:
            print("❌ O nome não pode ser vazio.")
            continue
        if not id:
            print("❌ O id não pode ser vazio.")
            continue
        if any(u["nome"].lower() == nome.lower() for u in lista):
            print("❌ Este projeto já está cadastrado!")
            continue

        novo_usuario = {"nome": nome, "id": id, "descrição": descrição, "inicio": inicio, "fim": fim}
        lista.append(novo_usuario)
        print("✅ projeto inserido com sucesso!")

    # ---------------------------
    # 2️ Listar projetos
    # ---------------------------
    elif(opcao==2):
        if not lista:
            print("não há projetos")
            opcao=10
        else:
            for a in lista:
                print(a)
        opcao=10

    # ---------------------------
    # 3️ Buscar projeto por nome (parcial)
    # ---------------------------
    elif opcao == 3:
        busca = input("Digite parte do nome para buscar: ").strip().lower()
        encontrados = [u for u in lista if busca in u["nome"].lower()]
        if encontrados:
            print("✅ projetos encontrados:")
            for u in encontrados:
                print(f"- {u['nome']} ({u['id']}) - descrição: {u['descrição']}")
        else:
            print("❌ Nenhum projeto encontrado!")

    # ---------------------------
    # 4️ Atualizar id e descrição
    # ---------------------------
    elif opcao == 4:
        busca = input("Digite o nome exato do projeto que deseja alterar: ").strip()
        encontrado = False
        for usuario in lista:
            if usuario["nome"].lower() == busca.lower():
                print("projeto atual:", usuario)
                novo_id = input("Novo id (vazio para manter): ").strip()
                novo_descrição = input("Novo descrição (vazio para manter): ").strip()

                if novo_id and any(u["id"].lower() == novo_id.lower() and u != usuario for u in lista):
                    print("❌ Este id já está em uso!")
                    break

                if novo_id:
                    usuario["id"] = novo_id
                if novo_descrição:
                    usuario["descrição"] = novo_descrição

                print("Dados atualizados com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("projeto não encontrado!")

    # ---------------------------
    # 5️ Remover um projeto
    # ---------------------------
    elif opcao == 5:
        remov = input("Digite o nome do projeto que deseja excluir: ").strip()
        for i, novo_usuario in enumerate(lista):
            if novo_usuario["nome"].lower() == remov.lower():
                print(" projeto removido:", novo_usuario)
                lista.pop(i)
                break
        else:
            print("projeto não encontrado!")

    # ---------------------------
    # 6️ Remover todos os projetos
    # ---------------------------
    elif opcao == 6:
        confirma = input("Tem certeza que deseja remover TODOS os projetos? (s/n): ").lower()
        if confirma == "s":
            lista.clear()
            print("Todos os projetos foram removidos!")
        else:
            print("Operação cancelada.")

    # ---------------------------
    # 0️ Sair e salvar
    # ---------------------------
    elif opcao == 0:
        print("💾 Salvando e encerrando...")
        salvar_usuarios(lista)
        print("✅ Dados salvos com sucesso! Até logo.")
        break

    # ---------------------------
    # Opção inválida
    # ---------------------------
    else:
        print("Opção inválida, tente novamente!")