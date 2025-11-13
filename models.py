from datetime import datetime

# Usuários
def criar_usuario(id, nome, email, perfil):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio")
    if "@" not in email:
        raise ValueError("E-mail inválido")
    return {"id": id, "nome": nome, "email": email, "perfil": perfil}

# Projetos
def criar_projeto(id, nome, descricao, inicio, fim):
    if not nome.strip():
        raise ValueError("Nome do projeto não pode ser vazio")
    data_inicio = datetime.strptime(inicio, "%Y-%m-%d")
    data_fim = datetime.strptime(fim, "%Y-%m-%d")
    if data_inicio > data_fim:
        raise ValueError("Data de início não pode ser maior que data de fim")
    return {"id": id, "nome": nome, "descricao": descricao, "inicio": inicio, "fim": fim}

# Tarefas
def criar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo):
    if not titulo.strip():
        raise ValueError("Título não pode ser vazio")
    if status not in ["pendente", "andamento", "concluída"]:
        raise ValueError("Status inválido")
    datetime.strptime(prazo, "%Y-%m-%d")  # valida formato
    return {
        "id": id,
        "titulo": titulo,
        "projeto_id": projeto_id,
        "responsavel_id": responsavel_id,
        "status": status,
        "prazo": prazo
    }