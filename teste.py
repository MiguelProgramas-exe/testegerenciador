import services 

# Cadastrar usuário
u1 = services.cadastrar_usuario("u_001", "Ariadne", "ariadne@ifsp.edu.br", "admin")
print("Usuário cadastrado:", u1)

# Cadastrar projeto
p1 = services.cadastrar_projeto("p_001", "RosenPy Docs", "Documentação do projeto", "2025-10-01", "2025-12-05")
print("Projeto cadastrado:", p1)

# Cadastrar tarefa
t1 = services.cadastrar_tarefa("t_001", "Escrever seção 3", "p_001", "u_001", "pendente", "2025-11-10")
print("Tarefa cadastrada:", t1)

# Listar tudo
print("Todos os usuários:", services.listar_usuarios())
print("Todos os projetos:", services.listar_projetos())
print("Todas as tarefas:", services.listar_tarefas())