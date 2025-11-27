from datetime import datetime

# ---------------------------------------------------------
# Valida se a data está no formato YYYY-MM-DD
# ---------------------------------------------------------
def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ---------------------------------------------------------
# Valida se data1 <= data2
# ---------------------------------------------------------
def data_menor_ou_igual(data1, data2):
    d1 = datetime.strptime(data1, "%Y-%m-%d")
    d2 = datetime.strptime(data2, "%Y-%m-%d")
    return d1 <= d2


# ---------------------------------------------------------
# Função genérica para pedir data com validação
# ---------------------------------------------------------
def input_data(prompt):
    while True:
        data = input(prompt).strip()
        if validar_data(data):
            return data
        print("Data inválida. Use o formato YYYY-MM-DD.")
 
        
def data_ordem(inicio, fim):
    contador=0
    ano=""
    mes=""
    dia=""
    for a in inicio:
        if(a != "-"):
            ano+=a
        else:
            break
    for a in inicio:
        contador+=1
        if(a != "-" and contador>5):
            mes+=a
        elif(contador<6):
            continue
        elif(contador>7):
            break
    contador=0
    for a in inicio:
        contador+=1
        if(a != "-" and contador>8):
            dia+=a
        elif(contador<9):
            continue
        else:
            break


    contador=0
    ano_fim=""
    mes_fim=""
    dia_fim=""
    for a in fim:
        if(a != "-"):
            ano_fim+=a
        else:
            break
    for a in fim:
        contador+=1
        if(a != "-" and contador>5):
            mes_fim+=a
        elif(contador<6):
            continue
        elif(contador>7):
            break
    contador=0
    for a in fim:
        contador+=1
        if(a != "-" and contador>8):
            dia_fim+=a
        elif(contador<9):
            continue
        else:
            break

    if(int(ano_fim)<int(ano)):
       condicao="invalido"
    elif(int(mes_fim)<int(mes) and int(ano_fim)==int(ano)):
        condicao="inválido"
    elif(int(dia_fim)<int(dia) and int(mes_fim)==int(mes) and int(ano_fim)==int(ano)):
        condicao="inválido"
    else:
        condicao="válido"
    return(condicao)
