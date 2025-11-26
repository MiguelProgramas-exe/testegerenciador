from datetime import datetime

def tarefas_atrasadas(tarefas):
    hoje = datetime.today().date()
    atrasadas = []

    for t in tarefas:
        prazo = datetime.strptime(t["prazo"], "%Y-%m-%d").date()
        if prazo < hoje and t["status"] != "concluída":
            atrasadas.append(t)

    return atrasadas


def tarefas_por_projeto(tarefas, projetos):
    relatorio = {}

    for projeto in projetos:
        relatorio[projeto["nome"]] = [
            t for t in tarefas if t["projeto_id"] == projeto["id"]
        ]

    return relatorio


def tarefas_por_responsavel(tarefas, usuarios):
    relatorio = {}

    for user in usuarios:
        relatorio[user["nome"]] = [
            t for t in tarefas if t["responsavel_id"] == user["id"]
        ]

    return relatorio


def percentual_conclusao_projeto(tarefas, projeto_id):
    tarefas_do_projeto = [t for t in tarefas if t["projeto_id"] == projeto_id]
    
    if not tarefas_do_projeto:
        return 0
    
    concluidas = [
        t for t in tarefas_do_projeto if t["status"] == "concluída"
    ]
    
    return (len(concluidas) / len(tarefas_do_projeto)) * 100
