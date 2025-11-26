from datetime import datetime

# Criação de registros com validação simples
def criar_usuario(id, nome, email, perfil):
    if not nome or not email:
        raise ValueError("Nome e email são obrigatórios")
    return {"id": id, "nome": nome, "email": email, "perfil": perfil}

def criar_projeto(id, nome, descricao, inicio, fim):
    if not nome:
        raise ValueError("Nome do projeto é obrigatório")
    if datetime.strptime(fim, "%Y-%m-%d") < datetime.strptime(inicio, "%Y-%m-%d"):
        raise ValueError("Data fim não pode ser anterior à data início")
    return {"id": id, "nome": nome, "descricao": descricao, "inicio": inicio, "fim": fim}

def criar_tarefa(id, titulo, projeto_id, responsavel_id, status, prazo):
    status = status.lower()
    if status not in ["pendente", "andamento", "concluída"]:
        raise ValueError("Status inválido")
    return {
        "id": id,
        "titulo": titulo,
        "projeto_id": projeto_id,
        "responsavel_id": responsavel_id,
        "status": status,
        "prazo": prazo
    }
