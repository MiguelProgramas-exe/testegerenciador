# services.py
import storage

# ============================================================
#                        USUÁRIOS
# ============================================================

def cadastrar_usuario(id, nome, email, perfil):
    usuarios = storage.load("usuarios")

    # email único
    if any(u["email"].lower() == email.lower() for u in usuarios):
        raise ValueError("Email já cadastrado.")

    novo = {
        "id": str(id),
        "nome": nome,
        "email": email,
        "perfil": perfil
    }

    usuarios.append(novo)
    storage.save("usuarios", usuarios)
    return novo


def listar_usuarios():
    return storage.load("usuarios")


def buscar_usuario_por_id(uid):
    usuarios = storage.load("usuarios")
    return next((u for u in usuarios if str(u["id"]) == str(uid)), None)


# ============================================================
#                        PROJETOS
# ============================================================

def cadastrar_projeto(id, nome, descricao, inicio, fim):
    projetos = storage.load("projetos")

    # nome único
    if any(p["nome"].lower() == nome.lower() for p in projetos):
        raise ValueError("Já existe um projeto com esse nome.")

    # ID único
    if any(str(p["id"]) == str(id) for p in projetos):
        raise ValueError("ID de projeto já existe.")

    novo = {
        "id": str(id),
        "nome": nome,
        "descricao": descricao,
        "inicio": inicio,
        "fim": fim
    }

    projetos.append(novo)
    storage.save("projetos", projetos)
    return novo


def listar_projetos():
    return storage.load("projetos")


def buscar_projeto_por_id(pid):
    projetos = storage.load("projetos")
    return next((p for p in projetos if str(p["id"]) == str(pid)), None)


def atualizar_projeto(nome_original, novo_nome=None, nova_desc=None, novo_inicio=None, novo_fim=None):
    projetos = storage.load("projetos")

    for p in projetos:
        if p["nome"].lower() == nome_original.lower():

            # valida nome novo
            if novo_nome:
                if any(other["nome"].lower() == novo_nome.lower() and other is not p for other in projetos):
                    raise ValueError("Já existe outro projeto com esse nome.")
                p["nome"] = novo_nome

            if nova_desc:
                p["descricao"] = nova_desc

            if novo_inicio:
                p["inicio"] = novo_inicio

            if novo_fim:
                p["fim"] = novo_fim

            storage.save("projetos", projetos)
            return p

    return None


def remover_projeto(nome):
    projetos = storage.load("projetos")

    for p in projetos:
        if p["nome"].lower() == nome.lower():
            projetos.remove(p)
            storage.save("projetos", projetos)
            return p

    return None


def remover_todos_projetos():
    storage.save("projetos", [])
    return True


# ============================================================
#                        TAREFAS
# ============================================================

def cadastrar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo):
    tarefas = storage.load("tarefas")

    # ID único
    if any(str(t["id"]) == str(id) for t in tarefas):
        raise ValueError("Já existe uma tarefa com esse id.")

    # valida projeto existe
    if not buscar_projeto_por_id(projeto_id):
        raise ValueError("Projeto não encontrado (projeto_id inválido).")

    novo = {
        "id": str(id),
        "titulo": titulo,
        "projeto_id": str(projeto_id),
        "responsavel_id": responsavel_id,
        "status": status,
        "prazo": prazo
    }

    tarefas.append(novo)
    storage.save("tarefas", tarefas)
    return novo


def listar_tarefas():
    return storage.load("tarefas")


def buscar_tarefa_por_id(tid):
    tarefas = storage.load("tarefas")
    return next((t for t in tarefas if str(t["id"]) == str(tid)), None)


def atualizar_tarefa(id, novo_titulo=None, novo_status=None, novo_prazo=None, novo_responsavel=None):
    tarefas = storage.load("tarefas")

    for t in tarefas:
        if str(t["id"]) == str(id):

            if novo_titulo:
                t["titulo"] = novo_titulo

            if novo_status:
                t["status"] = novo_status

            if novo_prazo:
                t["prazo"] = novo_prazo

            if novo_responsavel:
                t["responsavel_id"] = novo_responsavel

            storage.save("tarefas", tarefas)
            return t

    return None


def remover_tarefa(id):
    tarefas = storage.load("tarefas")

    for t in tarefas:
        if str(t["id"]) == str(id):
            tarefas.remove(t)
            storage.save("tarefas", tarefas)
            return t

    return None


def remover_todas_tarefas():
    storage.save("tarefas", [])
    return True

