import storage
import models

# ---------- Usuários ----------
def cadastrar_usuario(id, nome, email, perfil):
    usuarios = storage.read_json("usuarios")
    if any(u["email"] == email for u in usuarios):
        raise ValueError("E-mail já cadastrado")
    usuario = models.criar_usuario(id, nome, email, perfil)
    usuarios.append(usuario)
    storage.write_json("usuarios", usuarios)
    return usuario

def listar_usuarios():
    return storage.read_json("usuarios")

def buscar_usuario_por_email(email):
    usuarios = storage.read_json("usuarios")
    for u in usuarios:
        if u["email"] == email:
            return u
    return None

# ---------- Projetos ----------
def cadastrar_projeto(id, nome, descricao, inicio, fim):
    projetos = storage.read_json("projetos")
    if any(p["nome"] == nome for p in projetos):
        raise ValueError("Nome do projeto já existe")
    projeto = models.criar_projeto(id, nome, descricao, inicio, fim)
    projetos.append(projeto)
    storage.write_json("projetos", projetos)
    return projeto

def listar_projetos():
    return storage.read_json("projetos")

def buscar_projeto_por_nome(nome):
    projetos = storage.read_json("projetos")
    for p in projetos:
        if p["nome"] == nome:
            return p
    return None

# ---------- Tarefas ----------
def cadastrar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo):
    tarefas = storage.read_json("tarefas")
    tarefa = models.criar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo)
    tarefas.append(tarefa)
    storage.write_json("tarefas", tarefas)
    return tarefa

def listar_tarefas():
    return storage.read_json("tarefas")

def buscar_tarefas_por_status(status):
    tarefas = storage.read_json("tarefas")
    return [t for t in tarefas if t["status"] == status]

def buscar_tarefas_por_responsavel(responsavel_id):
    tarefas = storage.read_json("tarefas")
    return [t for t in tarefas if t["responsavel_id"] == responsavel_id]

def buscar_tarefas_por_projeto(projeto_id):
    tarefas = storage.read_json("tarefas")
    return [t for t in tarefas if t["projeto_id"] == projeto_id]
