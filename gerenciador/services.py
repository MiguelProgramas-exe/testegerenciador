import storage

# -------------------------
# USUÁRIOS
# -------------------------
def cadastrar_usuario(id, nome, email, perfil):
    usuarios = storage.load("usuarios")
    if any(u["email"] == email for u in usuarios):
        raise ValueError("Email já cadastrado.")
    novo = {"id": id, "nome": nome, "email": email, "perfil": perfil}
    usuarios.append(novo)
    storage.save("usuarios", usuarios)
    return novo

def listar_usuarios():
    return storage.load("usuarios")

def atualizar_usuario(email, novo_nome, novo_email, novo_perfil):
    usuarios = storage.load("usuarios")
    for u in usuarios:
        if u["email"] == email:
            if novo_nome:
                u["nome"] = novo_nome
            if novo_email:
                u["email"] = novo_email
            if novo_perfil:
                u["perfil"] = novo_perfil
            storage.save("usuarios", usuarios)
            return u
    return None

def remover_usuario(email):
    usuarios = storage.load("usuarios")
    for u in usuarios:
        if u["email"] == email:
            usuarios.remove(u)
            storage.save("usuarios", usuarios)
            return u
    return None


# -------------------------
# PROJETOS
# -------------------------
def cadastrar_projeto(id, nome, desc, inicio, fim):
    projetos = storage.load("projetos")
    novo = {"id": id, "nome": nome, "descricao": desc, "inicio": inicio, "fim": fim}
    projetos.append(novo)
    storage.save("projetos", projetos)
    return novo

def listar_projetos():
    return storage.load("projetos")

def atualizar_projeto(nome, novo_nome, nova_desc, novo_inicio, novo_fim):
    projetos = storage.load("projetos")
    for p in projetos:
        if p["nome"] == nome:
            if novo_nome:
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
        if p["nome"] == nome:
            projetos.remove(p)
            storage.save("projetos", projetos)
            return p
    return None


# -------------------------
# TAREFAS
# -------------------------
def cadastrar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo):
    tarefas = storage.load("tarefas")
    novo = {"id": id, "titulo": titulo, "projeto_id": projeto_id,
            "responsavel_id": responsavel_id, "status": status, "prazo": prazo}
    tarefas.append(novo)
    storage.save("tarefas", tarefas)
    return novo

def listar_tarefas():
    return storage.load("tarefas")

def atualizar_tarefa(id, novo_titulo, novo_status, novo_prazo):
    tarefas = storage.load("tarefas")
    for t in tarefas:
        if t["id"] == id:
            if novo_titulo:
                t["titulo"] = novo_titulo
            if novo_status:
                t["status"] = novo_status
            if novo_prazo:
                t["prazo"] = novo_prazo
            storage.save("tarefas", tarefas)
            return t
    return None
    
def remover_tarefa(id):
    tarefas = storage.load("tarefas")
    for t in tarefas:
        if t["id"] == id:
            tarefas.remove(t)
            storage.save("tarefas", tarefas)
            return t
    return None


