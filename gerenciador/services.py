import storage
import models
from utils import validar_email, validar_data, data_menor_ou_igual

# ============================================================
#                      USUÁRIOS
# ============================================================

def cadastrar_usuario(id, nome, email, perfil):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio")

    if not validar_email(email):
        raise ValueError("E-mail inválido")

    usuarios = storage.read_json("usuarios")

    if any(u["email"] == email for u in usuarios):
        raise ValueError("E-mail já cadastrado")

    if any(u["id"] == id for u in usuarios):
        raise ValueError("ID já cadastrado")

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


def atualizar_usuario(id, novo_nome=None, novo_email=None, novo_perfil=None):
    usuarios = storage.read_json("usuarios")

    for u in usuarios:
        if u["id"] == id:

            if novo_nome:
                if not novo_nome.strip():
                    raise ValueError("Nome não pode ser vazio")
                u["nome"] = novo_nome

            if novo_email:
                if not validar_email(novo_email):
                    raise ValueError("E-mail inválido")
                if any(user["email"] == novo_email for user in usuarios if user != u):
                    raise ValueError("E-mail já cadastrado")
                u["email"] = novo_email

            if novo_perfil:
                u["perfil"] = novo_perfil

            storage.write_json("usuarios", usuarios)
            return u

    return None


def remover_usuario(id):
    usuarios = storage.read_json("usuarios")

    for i, u in enumerate(usuarios):
        if u["id"] == id:
            usuarios.pop(i)
            storage.write_json("usuarios", usuarios)
            return u
    return None


# ============================================================
#                      PROJETOS
# ============================================================

def cadastrar_projeto(id, nome, descricao, inicio, fim):
    projetos = storage.read_json("projetos")

    if any(p["id"] == id for p in projetos):
        raise ValueError("ID do projeto já existe")

    if any(p["nome"] == nome for p in projetos):
        raise ValueError("Já existe um projeto com esse nome")

    if not validar_data(inicio) or not validar_data(fim):
        raise ValueError("Datas inválidas (use YYYY-MM-DD)")

    if not data_menor_ou_igual(inicio, fim):
        raise ValueError("Data de início deve ser <= data de fim")

    projeto = models.criar_projeto(id, nome, descricao, inicio, fim)
    projetos.append(projeto)
    storage.write_json("projetos", projetos)
    return projeto


def listar_projetos():
    return storage.read_json("projetos")


def buscar_projeto_por_id(id):
    projetos = storage.read_json("projetos")
    for p in projetos:
        if p["id"] == id:
            return p
    return None


def atualizar_projeto(id, novo_nome=None, nova_descricao=None, novo_inicio=None, novo_fim=None):
    projetos = storage.read_json("projetos")

    for p in projetos:
        if p["id"] == id:

            if novo_nome:
                if any(proj["nome"] == novo_nome for proj in projetos if proj != p):
                    raise ValueError("Já existe outro projeto com esse nome")
                p["nome"] = novo_nome

            if nova_descricao:
                p["descricao"] = nova_descricao

            if novo_inicio:
                if not validar_data(novo_inicio):
                    raise ValueError("Data inválida")
                p["inicio"] = novo_inicio

            if novo_fim:
                if not validar_data(novo_fim):
                    raise ValueError("Data inválida")
                p["fim"] = novo_fim

            # Validar consistência
            if not data_menor_ou_igual(p["inicio"], p["fim"]):
                raise ValueError("Data de início não pode ser maior que data de fim")

            storage.write_json("projetos", projetos)
            return p

    return None


def remover_projeto(id):
    projetos = storage.read_json("projetos")

    for i, p in enumerate(projetos):
        if p["id"] == id:
            projetos.pop(i)
            storage.write_json("projetos", projetos)
            return p
    return None


# ============================================================
#                      TAREFAS
# ============================================================

STATUS_VALIDOS = ["pendente", "andamento", "concluída"]

def cadastrar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo):
    tarefas = storage.read_json("tarefas")

    if any(t["id"] == id for t in tarefas):
        raise ValueError("ID da tarefa já existe")

    if not titulo.strip():
        raise ValueError("Título não pode ser vazio")

    if status not in STATUS_VALIDOS:
        raise ValueError(f"Status inválido. Use: {STATUS_VALIDOS}")

    if not validar_data(prazo):
        raise ValueError("Prazo inválido")

    # Verificar se projeto existe
    if not buscar_projeto_por_id(projeto_id):
        raise ValueError("Projeto não encontrado")

    # Verificar se usuário existe
    usuarios = listar_usuarios()
    if not any(u["id"] == responsavel_id for u in usuarios):
        raise ValueError("Responsável não encontrado")

    tarefa = models.criar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo)
    tarefas.append(tarefa)
    storage.write_json("tarefas", tarefas)
    return tarefa


def listar_tarefas():
    return storage.read_json("tarefas")


def buscar_tarefas_por_status(status):
    return [t for t in listar_tarefas() if t["status"] == status]


def buscar_tarefas_por_responsavel(responsavel_id):
    return [t for t in listar_tarefas() if t["responsavel_id"] == responsavel_id]


def buscar_tarefas_por_projeto(projeto_id):
    return [t for t in listar_tarefas() if t["projeto_id"] == projeto_id]


def atualizar_tarefa(id, novo_titulo=None, novo_status=None, novo_prazo=None, novo_responsavel=None):
    tarefas = storage.read_json("tarefas")

    for t in tarefas:
        if t["id"] == id:

            if novo_titulo:
                if not novo_titulo.strip():
                    raise ValueError("Título não pode ser vazio")
                t["titulo"] = novo_titulo

            if novo_status:
                if novo_status not in STATUS_VALIDOS:
                    raise ValueError(f"Status inválido. Use {STATUS_VALIDOS}")
                t["status"] = novo_status

            if novo_prazo:
                if not validar_data(novo_prazo):
                    raise ValueError("Prazo inválido")
                t["prazo"] = novo_prazo

            if novo_responsavel:
                usuarios = listar_usuarios()
                if not any(u["id"] == novo_responsavel for u in usuarios):
                    raise ValueError("Responsável não encontrado")
                t["responsavel_id"] = novo_responsavel

            storage.write_json("tarefas", tarefas)
            return t

    return None


def remover_tarefa(id):
    tarefas = storage.read_json("tarefas")
    for i, t in enumerate(tarefas):
        if t["id"] == id:
            tarefas.pop(i)
            storage.write_json("tarefas", tarefas)
            return t
    return None


# ============================================================
#           Regras: Concluir e Reabrir Tarefas
# ============================================================

def concluir_tarefa(id):
    return atualizar_tarefa(id, novo_status="concluída")


def reabrir_tarefa(id):
    return atualizar_tarefa(id, novo_status="pendente")
